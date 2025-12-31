package com.example.app

class Cat(val name: String = "Lil Boo Thang", val age: Int = 5)

interface CatInfoProvider{
    fun printInfo(cat: Cat){

    }
}

class BasicInfoProvider : CatInfoProvider {
    override fun printInfo(cat: Cat) {
        println("Cat's name is: ${cat.name}, age: ${cat.age}")
    }
}

fun main() {
    val provider = BasicInfoProvider()
    provider.printInfo(Cat())
}