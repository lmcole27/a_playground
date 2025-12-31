package com.example.app

class Person(val firstName: String = "Beanie", val lastName: String = "Boo"){

    var nickName: String? = "Kitty"
        set(value) {
            field = value
            //println("nickName was set to $value")
        }
        get(){
            //println("nickName $field was retrieved")
            return field
        }
        fun printInfo(){
            var nickNameToPrint = nickName ?: ""
            println("$firstName $nickNameToPrint $lastName")
        }
    // init {
    //     println("1")
    // }
    // constructor(): this("Medusa", "Codes"){
    //     println("secondary constructor called")
    // } 
    // init {
    //     println("2")
    // }
}