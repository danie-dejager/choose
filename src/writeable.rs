pub trait Writeable: Copy {
    fn to_byte_buf(&self) -> Box<[u8]>;
    fn is_empty(&self) -> bool;
}

impl Writeable for &str {
    fn to_byte_buf(&self) -> Box<[u8]> {
        return Box::from(self.as_bytes());
    }
    
    fn is_empty(&self) -> bool {
        str::is_empty(&self)
    }
}

impl Writeable for char {
    fn to_byte_buf(&self) -> Box<[u8]> {
        let mut buf = [0; 4];
        return self
            .encode_utf8(&mut buf)
            .to_owned()
            .into_boxed_str()
            .into_boxed_bytes();
    }

    fn is_empty(&self) -> bool {
        return false
    }
}
