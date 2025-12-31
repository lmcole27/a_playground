package com.example.app

fun main() {
    val person = Person()
    //val person = Person(firstName = "John", lastName = "Doe")
    //person.nickName = "JD"
    //person.nickName = "Cute Kitty"
    person.printInfo()
    //println("Person's name is: ${person.firstName} ${person.lastName} ${person.nickName}")
    val provider = BasicInfoProvider()
    provider.printInfo(Cat())
}