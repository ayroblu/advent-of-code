use std::fs;
use std::path::PathBuf;

// https://stackoverflow.com/questions/47302294/is-there-a-macro-or-similar-workaround-to-include-the-source-folder-src-path-a
#[macro_export]
macro_rules! file_abs {
    () => {
        std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join(file!())
    };
}

pub fn read_file(file_path: PathBuf) -> String {
    let path_name = file_path.parent().unwrap().join("input");
    return fs::read_to_string(path_name).unwrap();
}
