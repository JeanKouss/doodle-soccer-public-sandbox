#!/bin/sh
echo -ne '\033c\033]0;doodle-project\a'
base_path="$(dirname "$(realpath "$0")")"
"$base_path/doodle_soccer.x86_64" "$@"
