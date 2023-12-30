Advent Of Code
==============

https://adventofcode.com

2023
----
Mostly doing python, this helped me to figure out my neovim editor settings cause they don't work out of the box like VSCode.
Also relearning a bit of the python fundamentals

Also running rust cause I think I can write the same python code in rust.

### Getting started python

This should setup everything.

```sh
poetry install
```

Typechecking should be automatically handled by pyright when using it as an LSP such as for vim.

There are two options for running some python file.

```sh
poetry shell
python "<path-here>"
# OR
# Note this has a 280ms setup time
poetry run python "<path-here>"
```

### Getting started rust

All rust programs are self organised (e.g. type errors in one won't affect another). All programs are defined in the Cargo.toml. To run simply use `cargo run --bin <program-name>`. Note that for performance, consider using the `--release` flag for better performance, and you can run the binary afterwards at `target/release/<program-name>`.
