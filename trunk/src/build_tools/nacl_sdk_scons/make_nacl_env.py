# -*- python -*-
#
# Copyright (c) 2011 The Native Client Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

'''Construct an Environment that uses the NaCl toolchain to build C/C++ code.
The base dir for the NaCl toolchain is in the NACL_SDK_ROOT environment
variable.
'''

import nacl_utils
import os

from SCons import Script

def NaClEnvironment(use_c_plus_plus_libs=False):
  '''Make an Environment that uses the NaCl toolchain to build sources.

  This modifies a default construction Environment to point the compilers and
  other bintools at the NaCl-specific versions, adds some tools that set certain
  build flags needed by the NaCl-specific tools, and adds a custom Builder that
  generates .nmf files.

  Args:
    use_c_plus_plus_libs: Indicate whether to insert the C++ NaCl libs at the
        right place in the list of LIBS.
  Returns:
    A SCons Environment with all the various Tool and keywords set to build
    NaCl modules.
  '''

  toolchain = nacl_utils.FindToolchain()
  if (toolchain is None):
    raise ValueError('Cannot find a NaCl toolchain')

  tool_bin_path = os.path.join(toolchain, 'bin')

  env = Script.Environment()

  # Invoke the various *nix tools that the NativeClient SDK resembles.  This
  # is done so that SCons doesn't try to invoke cl.exe on Windows in the
  # Object builder.
  env.Tool('g++')
  env.Tool('gcc')
  env.Tool('gnulink')
  env.Tool('ar')
  env.Tool('as')

  env.Tool('nacl_tools')
  # TODO(dspringer): Figure out how to make this dynamic and then compute it
  # based on the desired target arch.
  env.Replace(tools=['nacl_tools'],
              # Replace the normal unix tools with the NaCl ones.  Note the
              # use of the NACL_ARCHITECTURE prefix for the tools.  This
              # Environment variable is set in nacl_tools.py; it has no
              # default value.
              CC=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}gcc'),
              CXX=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}g++'),
              AR=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}ar'),
              AS=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}as'),
              GDB=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}gdb'),
              # NOTE: use g++ for linking so we can handle C AND C++.
              LINK=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}g++'),
              LD=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}ld'),
              NACL_SEL_LDR32=os.path.join(tool_bin_path, 'sel_ldr_x86_32'),
              NACL_SEL_LDR64=os.path.join(tool_bin_path, 'sel_ldr_x86_64'),
              RANLIB=os.path.join(tool_bin_path, '${NACL_ARCHITECTURE}ranlib'),
              ASFLAGS=['${EXTRA_ASFLAGS}',
                      ],
              # c specific
              EXTRA_CFLAGS=[],
              CFLAGS=['${EXTRA_CFLAGS}',
                      '-std=gnu99',
                      ],
              # c++ specific
              EXTRA_CXXFLAGS=[],
              CXXFLAGS=['${EXTRA_CXXFLAGS}',
                        '-std=gnu++98',
                        '-Wno-long-long',
                        ],
              # Both C and C++
              CCFLAGS=['${EXTRA_CCFLAGS}',
                       '-Wall',
                       '-Wswitch-enum',
                       '-pthread',
                      ],
              CPPDEFINES=[# _GNU_SOURCE ensures that strtof() gets declared.
                         ('_GNU_SOURCE', 1),
                         # This ensures that PRId64 etc. get defined.
                         ('__STDC_FORMAT_MACROS', '1'),
                         # strdup, and other common stuff
                         ('_BSD_SOURCE', '1'),
                         ('_POSIX_C_SOURCE', '199506'),
                         ('_XOPEN_SOURCE', '600'),
                         ],
              CPPPATH=[],
              LINKFLAGS=['${EXTRA_LINKFLAGS}',
                        ],
              # The NaCl envorinment makes '.nexe' executables.  If this is
              # not explicitly set, then SCons on Windows doesn't understand
              # how to construct a Program builder properly.
              PROGSUFFIX='.nexe',
             )
  # This supresses the "MS_DOS style path" warnings on Windows.  It's benign on
  # all other platforms.
  env['ENV']['CYGWIN'] = 'nodosfilewarning'

  # Append the common NaCl libs.
  common_nacl_libs = ['ppapi']
  if use_c_plus_plus_libs:
    common_nacl_libs.extend(['ppapi_cpp'])
  env.Append(LIBS=common_nacl_libs)

  gen_nmf_builder = env.Builder(suffix='.nmf',
                                action=nacl_utils.GenerateNmf)
  env.Append(BUILDERS={'GenerateNmf': gen_nmf_builder})

  return env