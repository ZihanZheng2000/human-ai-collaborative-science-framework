param(
    [Parameter(Mandatory = $true)]
    [string]$ReviewRequestPath,

    [string]$CritiquePath,

    [string]$ClaudeCommand = "claude",

    [switch]$Overwrite
)

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$requestFullPath = (Resolve-Path -LiteralPath $ReviewRequestPath).Path

if (-not $CritiquePath) {
    $requestDir = Split-Path -Parent $requestFullPath
    $CritiquePath = Join-Path $requestDir "reviewer-critique.md"
}

$critiqueFullPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($CritiquePath)
if ((Test-Path -LiteralPath $critiqueFullPath) -and -not $Overwrite) {
    throw "Critique file already exists: $critiqueFullPath. Pass -Overwrite to replace it."
}

$prompt = @"
You are the reviewer agent for this repository.

Work from this repository root:
$repoRoot

Required behavior:
1. Read CLAUDE.md and follow the Reviewer role section.
2. Read docs/decision-rights.md, docs/coordination.md, and docs/reviewer-agents/cross-agent-handoff.md.
3. Read the Header and Artifacts to Inspect sections of this review request:
$requestFullPath
4. Check the assignment. The request header is authoritative for this pass. If it names a reviewer other than Claude Code, or names Claude Code while WORKFLOW-CONFIG.md assigns a different reviewer and the header does not cite a user override decision, still write the critique, but make the assignment mismatch the first finding (severity major, route user decision).
5. Read the relevant stage reviewer-agent file, the stage package, the decision log, and the listed artifacts.
6. If the review mode is blind, write independent findings before reading the Researcher Framing section, then add follow-up findings in a separate block. If standard, read the Researcher Framing section before critiquing.
7. Write your critique to this exact path:
$critiqueFullPath

Use the critique format in docs/reviewer-agents/cross-agent-handoff.md.
Do not edit the stage package, docs, templates, decision log, or supporting artifacts.
If the request is incomplete, still write the critique file and record the gap as a finding.
"@

Push-Location $repoRoot
try {
    & $ClaudeCommand -p $prompt
    $exitCode = $LASTEXITCODE
}
finally {
    Pop-Location
}

if ($exitCode -ne 0) {
    throw "Claude reviewer command failed with exit code $exitCode."
}

if (-not (Test-Path -LiteralPath $critiqueFullPath)) {
    throw "Claude command completed, but critique file was not created: $critiqueFullPath"
}

Write-Output "Reviewer critique written: $critiqueFullPath"
