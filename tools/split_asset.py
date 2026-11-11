import argparse
import hashlib
from pathlib import Path


def split(source: Path, destination: Path, expected: str) -> None:
    limit = 2 * 1024**3
    chunk_size = 1536 * 1024**2
    size = source.stat().st_size
    if size <= 0:
        raise ValueError("Source must not be empty")
    destination.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    assets = []
    with source.open("rb") as original:
        remaining = size
        while remaining:
            part_size = min(remaining, chunk_size) if size >= limit else size
            name = source.name if size < limit else f"{source.name}.part{len(assets) + 1:02}"
            path = destination / name
            with path.open("wb") as part:
                unwritten = part_size
                while unwritten:
                    data = original.read(min(unwritten, 1024**2))
                    if not data:
                        raise OSError("Source ended early")
                    part.write(data)
                    digest.update(data)
                    unwritten -= len(data)
            assets.append(path)
            remaining -= part_size
        if original.read(1) or digest.hexdigest() != expected.lower():
            raise ValueError("Source does not match the expected SHA-256; do not upload")
    for path in assets:
        print(f"{path.name}: {path.stat().st_size} bytes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare byte-exact GitHub Release attachments")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("sha256")
    args = parser.parse_args()
    split(args.source, args.destination, args.sha256)
