let Levenshtein str1 str2 = 
    let n = String.length str1
    let m = String.length str2
    let mutable k = 0
    let prev_array = Array.zeroCreate (n + 1)
    let curr_array = Array.zeroCreate (n + 1)
    for i = 1 to n do
        prev_array[i] <- i
    done
    
    for i = 1 to m do
        curr_array[0] <- prev_array[0] + 1
        for j = 1 to n do
            if str1[j - 1] = str2[i - 1] then k <- 0 else  k <- 1
            curr_array[j] <- System.Math.Min(prev_array[j - 1] + k, System.Math.Min(curr_array[j - 1] + 1, prev_array[j] + 1))
            prev_array[j - 1] <- curr_array[j - 1]
        done
        prev_array[n] <- curr_array[n]
    curr_array[n]
    

let str1 = "bibao"
let str2 = "bobaoooooo"
let result = Levenshtein str1 str2
printfn "%d" result