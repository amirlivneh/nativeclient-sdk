﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.269
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace NativeClientVSAddIn {
    using System;
    
    
    /// <summary>
    ///   A strongly-typed resource class, for looking up localized strings, etc.
    /// </summary>
    // This class was auto-generated by the StronglyTypedResourceBuilder
    // class via a tool like ResGen or Visual Studio.
    // To add or remove a member, edit your .ResX file then rerun ResGen
    // with the /str option, or rebuild your VS project.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "4.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    internal class Strings {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Strings() {
        }
        
        /// <summary>
        ///   Returns the cached ResourceManager instance used by this class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("NativeClientVSAddIn.Strings", typeof(Strings).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Overrides the current thread's CurrentUICulture property for all
        ///   resource lookups using this strongly typed resource class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Native Client Visual Studio Add-In.
        /// </summary>
        internal static string AddInName {
            get {
                return ResourceManager.GetString("AddInName", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to CHROME_PATH.
        /// </summary>
        internal static string ChromePathEnvironmentVariable {
            get {
                return ResourceManager.GetString("ChromePathEnvironmentVariable", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to chrome.exe.
        /// </summary>
        internal static string ChromeProcessName {
            get {
                return ResourceManager.GetString("ChromeProcessName", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to --type=renderer.
        /// </summary>
        internal static string ChromeRendererFlag {
            get {
                return ResourceManager.GetString("ChromeRendererFlag", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Warning: Multiple start-up projects not supported. Web server will only be run from first project directory.
        /// </summary>
        internal static string MultiStartProjectWarning {
            get {
                return ResourceManager.GetString("MultiStartProjectWarning", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to --enable-nacl-debug.
        /// </summary>
        internal static string NaClDebugFlag {
            get {
                return ResourceManager.GetString("NaClDebugFlag", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to --type=nacl-loader.
        /// </summary>
        internal static string NaClLoaderFlag {
            get {
                return ResourceManager.GetString("NaClLoaderFlag", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to NaCl.
        /// </summary>
        internal static string NaClPlatformName {
            get {
                return ResourceManager.GetString("NaClPlatformName", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to nacl64.exe.
        /// </summary>
        internal static string NaClProcessName {
            get {
                return ResourceManager.GetString("NaClProcessName", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to PPAPI.
        /// </summary>
        internal static string PepperPlatformName {
            get {
                return ResourceManager.GetString("PepperPlatformName", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to --register-pepper-plugins=&quot;{0};application/x-nacl&quot;.
        /// </summary>
        internal static string PepperProcessPluginFlagFormat {
            get {
                return ResourceManager.GetString("PepperProcessPluginFlagFormat", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to NACL_SDK_ROOT.
        /// </summary>
        internal static string SDKPathEnvironmentVariable {
            get {
                return ResourceManager.GetString("SDKPathEnvironmentVariable", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to NaCl SDK Root is not set in project properties! Cannot run NaCl functionality..
        /// </summary>
        internal static string SDKPathNotSetError {
            get {
                return ResourceManager.GetString("SDKPathNotSetError", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Unsupported breakpoint type: {0}.
        /// </summary>
        internal static string UnsupportedBreakpointTypeFormat {
            get {
                return ResourceManager.GetString("UnsupportedBreakpointTypeFormat", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Native Client Web Server Output.
        /// </summary>
        internal static string WebServerOutputWindowTitle {
            get {
                return ResourceManager.GetString("WebServerOutputWindowTitle", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Specified web server port was not valid, defaulting to {0}.
        /// </summary>
        internal static string WebServerPortNotSetFormat {
            get {
                return ResourceManager.GetString("WebServerPortNotSetFormat", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Warning: Failed to start web server. Is python.exe in PATH?.
        /// </summary>
        internal static string WebServerStartFail {
            get {
                return ResourceManager.GetString("WebServerStartFail", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Launching web server....
        /// </summary>
        internal static string WebServerStartMessage {
            get {
                return ResourceManager.GetString("WebServerStartMessage", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to Killing web server....
        /// </summary>
        internal static string WebServerStopMessage {
            get {
                return ResourceManager.GetString("WebServerStopMessage", resourceCulture);
            }
        }
    }
}
