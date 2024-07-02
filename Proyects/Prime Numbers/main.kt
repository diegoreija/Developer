

fun main() {

    (1..100).forEach { number ->
        if (isPrime(number)) {
            println(number)
        }
    }
}

private fun isPrime(number: Int): Boolean {
    if (number < 2) {
        return false
    }

    for (i in 2 until number) {
        if (number % i == 0) {
            return false
        }
    }
    return true
}
