$ErrorActionPreference = 'Stop'
$drawioExe = 'C:\Program Files\draw.io\draw.io.exe'
$diagramDirectory = Join-Path (Split-Path $PSScriptRoot -Parent) 'Sơ đồ kiến trúc'
$diagrams = Get-ChildItem -LiteralPath $diagramDirectory -Filter '*.drawio' | Where-Object { $_.Name -notlike '00-*' }
foreach ($diagram in $diagrams) {
    foreach ($format in @('png','svg')) {
        $target = $diagram.FullName + '.' + $format
        $exportArgs = @('--disable-gpu','-x','-f',$format,'-e','-b','25','-o',('"' + $target + '"'),('"' + $diagram.FullName + '"'))
        $proc = Start-Process -FilePath $drawioExe -ArgumentList $exportArgs -WindowStyle Hidden -Wait -PassThru
        if (-not (Test-Path -LiteralPath $target)) { throw "Export failed: $target exit $($proc.ExitCode)" }
    }
    Write-Output ('Exported ' + $diagram.Name)
}
