
import java.util.Scanner

fun main() {
    // Crear un objeto Scanner para leer la entrada del usuario
    val scanner = Scanner(System.`in`)

    var dato: String

    do {
        // Solicitar al usuario que ingrese un dato
        print("$~ ")

        // Leer la entrada del usuario
        dato = scanner.nextLine()

        if (dato != "FizzBuzz") {
            println("Entrada incorrecta...")
        }
    } while (dato != "FizzBuzz")

    // Una vez que el usuario ingrese "FizzBuzz"
    for (index in 1..100) {
        val divisibleByThree = index % 3 == 0
        val divisibleByFive = index % 5 == 0

        if (divisibleByThree && divisibleByFive) {
            println("fizzbuzz")
        } else if (divisibleByThree) {
            println("fizz")
        } else if (divisibleByFive) {
            println("buzz")
        } else {
            println(index)
        }
    }
}
