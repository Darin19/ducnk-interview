using System;
using System.Diagnostics;
using System.Text;

public static class SofficeShim
{
    private static string Quote(string value)
    {
        if (value == null) return "\"\"";
        return "\"" + value.Replace("\"", "\\\"") + "\"";
    }

    public static int Main(string[] args)
    {
        var command = new StringBuilder();
        foreach (var arg in args)
        {
            // LibreOffice 26.2 on this host crashes when a temporary
            // UserInstallation URI is supplied; use the local default profile.
            if (arg.StartsWith("-env:UserInstallation=", StringComparison.OrdinalIgnoreCase))
                continue;
            if (command.Length > 0) command.Append(' ');
            command.Append(Quote(arg));
        }

        var psi = new ProcessStartInfo
        {
            FileName = @"C:\Program Files\LibreOffice\program\soffice.com",
            Arguments = command.ToString(),
            UseShellExecute = false,
            RedirectStandardOutput = false,
            RedirectStandardError = false,
            CreateNoWindow = true
        };
        using (var process = Process.Start(psi))
        {
            process.WaitForExit();
            return process.ExitCode;
        }
    }
}
