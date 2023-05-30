
// TODO Part 1, function composition

// Given function composition
let (>>) f g x = g(f(x))

// Implement addition, multiplication and substraction

let add x y = x + y
let mul x y = x * y
let sub x y = y - x

printfn "PART 1"
// Compose it in order to get the expected result
// At least 2 composed functions:
printfn "Expected result: 9 == %d" ((add 0 >> mul 3) 3)
// At least 3 composed functions of each type:
printfn "Expected result: 85 == %d" ((add 4 >> mul 11 >> sub 3) 4)
// At least 5 composed functions of different types:
printfn "Expected result: 739 == %d" ((mul 50 >> mul 2 >> add 20 >> add 20 >> sub 1) 7)

// TODO Part 2, function composition

type Result<'TEntity> =
    | Success of 'TEntity
    | Failure of string


let bind switchFunction twoTrackInput =
    match twoTrackInput with
    | Success x -> switchFunction x
    | Failure f -> Failure f

let (>>=) twoTrackInput switchFunction = bind switchFunction twoTrackInput

let greatherThan num x =
    if x > num then
        Success x
    else Failure (sprintf "%d must be greather than %d" x num)

// Add more functions implementations
let lessThan num x =
    if x < num then
        Success x
    else Failure (sprintf "%d must be less than %d" x num)
let modulo num x =
    let res = x % num
    if res = 0 then
        Success x
    else Failure (sprintf "The remain of mod %d for is %d is %d " num x res)
let someDivisionBy num x =
    if num = 0 then Failure "Cannot divide by 0"
    else x / num |> Success

// Final function to use
let asString x = x |> sprintf "My final number is %d" |> Success

let railway x =
    match x |> Success
        >>= (greatherThan 9)
        >>= (lessThan 101)
        >>= (modulo 5)
        >>= (someDivisionBy 5)
        >>= (greatherThan 5)
        >>= asString with
    | Success s -> sprintf "Success: %s" s
    | Failure f -> sprintf "Failure: %s" f


printfn "\n\nPART 2"
printfn "All goes well - %s" (railway(75))
printfn "Too small number - %s" (railway(1))
printfn "Too great number - %s" (railway(150))
printfn "Mod issue - %s" (railway(77))
printfn "Too small after division - %s" (railway(25))
