#!/bin/bash
set -u
export PYTHONDONTWRITEBYTECODE=1
export GIT_OPTIONAL_LOCKS=0
artifact=/workspace/scratch/46b31bb4dff6/037-a014-authorized-consumer-artifacts
entry=$(date -u +%s%N)
printf '\nTIME %s\nCWD %s\nCOMMAND %s\nRAW STDOUT %s\nRAW STDERR %s\n' "$(date -u +%FT%TZ)" "$PWD" "$1" "$entry.stdout" "$entry.stderr" >> "$artifact/chronology.log"
bash -e -c "$1" > "$artifact/$entry.stdout" 2> "$artifact/$entry.stderr"
result=$?
cat "$artifact/$entry.stdout"
cat "$artifact/$entry.stderr" >&2
printf 'STATUS %s\n' "$result" >> "$artifact/chronology.log"
exit "$result"
