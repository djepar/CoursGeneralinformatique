//chapter 2 : doing Echo with Rust
use clap::{App, Arg};



fn main() {
    let matches = App::new("echor")
        .version("0.1.0")
        .author("Jeremie Paradis <jparadis21@hotmail.com>")
        .about("Rust echo")
        .arg(
            Arg::with_name("text")
                .value_name("TEXT")
                .help("Input text")
                .required(true)
                .min_values(1),
        )
        .arg(
            Arg::with_name("omit_newline")
                .short("n")
                .help("Do not print newline")
                .takes_value(false),
        )
        .get_matches();
        
    println!("{:#?}",matches);
    let text = vec!["Hello", "World!!!"];
    let text = matches.values_of_lossy("text").unwrap();
    let omit_newline = matches.is_present("omit_newline");
    println!("{}", text.join("")); //to join all of the vec values together. 
    
}