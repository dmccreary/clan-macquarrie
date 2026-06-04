#!/usr/bin/env bash
set -euo pipefail

ROOT="book"

# The eight chapter titles from the TOC (spelling preserved)
chapters=(
  "Introduction"
  "The Celtic Period"
  "Scotch History"
  "Lord of the Isles & Council of the Isles"
  "Begining & Development of the Clans"
  "MacQuarrie References"
  "Chief Lachlan(XVI)"
  "Major General Lachlan Macquarie"
)

slugify() {
  # lowercase, replace "&" with "and", remove apostrophes,
  # convert non-alphanumerics to hyphens, collapse repeats, trim edges
  echo "$1" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -e 's/&/ and /g' -e "s/'//g" \
    | sed -e 's/[^a-z0-9]+/-/g' -e 's/[^a-z0-9]/-/g' \
    | sed -e 's/-\{2,\}/-/g' -e 's/^-//' -e 's/-$//'
}

mkdir -p "$ROOT"

for i in "${!chapters[@]}"; do
  n=$((i+1))
  printf -v prefix "ch%02d" "$n"
  title="${chapters[$i]}"
  slug="$(slugify "$title")"
  dir="$ROOT/$prefix-$slug"
  mkdir -p "$dir"
  printf '# %s\n' "$title" > "$dir/index.md"
  echo "Created: $dir/index.md"
done

echo "All done in $ROOT/"

