param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments)

$convertIndex = [Array]::IndexOf($Arguments, '--convert-to')
$outDirIndex = [Array]::IndexOf($Arguments, '--outdir')
if ($convertIndex -lt 0 -or $outDirIndex -lt 0) {
    Write-Error 'Unsupported soffice invocation.'
    exit 2
}

$format = $Arguments[$convertIndex + 1]
$outDir = $Arguments[$outDirIndex + 1]
$inputPath = $Arguments[-1]
if ($format -ne 'pdf') {
    Write-Error "Only PDF export is supported by this local shim: $format"
    exit 3
}

$resolvedInput = (Resolve-Path -LiteralPath $inputPath).Path
$resolvedOutDir = (Resolve-Path -LiteralPath $outDir).Path
$outputPath = Join-Path $resolvedOutDir (([IO.Path]::GetFileNameWithoutExtension($resolvedInput)) + '.pdf')

$word = $null
$doc = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.ScreenUpdating = $false
    $word.Options.UpdateLinksAtOpen = $false
    $doc = $word.Documents.Open($resolvedInput, $false, $true)
    $doc.ExportAsFixedFormat($outputPath, 17)
    Write-Output "convert $resolvedInput -> $outputPath"
}
catch {
    Write-Error $_
    exit 4
}
finally {
    if ($null -ne $doc) {
        $doc.Close($false)
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc)
    }
    if ($null -ne $word) {
        $word.Quit()
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
