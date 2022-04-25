fn main() {
    let _s1 = gives_ownership();  //gives_ownership moves its return
                                //return value into s1;
    let s2 = String::from("hello");   //s2 comes into scope

    let _s3 = takes_and_gives_back(s2);  //s2 is moved into 
                                        //takes_and_gives_back, which also
                                        //moves its return value into s3
} //Here, s3 goes out of scope and is dropped. S2 was moved, so nothing happends. 
// s1 goes out of scope and is dropped. 

fn gives_ownership() -> String {    // gives_ownership will move its
                                    // return value into the function
                                    // that calls it

    let some_string = String::from("yours");    //some_string comes into scope

    some_string //some_string is returned
                // and moves out to the calling function

}

//this function takes a String and returns one

fn takes_and_gives_back(a_string: String) -> String {  //a_string comes into scope

    a_string // a_string is returned and moves out to the calling function

}