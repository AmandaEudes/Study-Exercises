# Create an implementation of the Atbash cipher, an ancient encryption system
# created in the Middle East.

# The Atbash cipher is a simple substitution cipher that relies on transposing
# all the letters in the alphabet such that the resulting alphabet is backwards.
# The first letter is replaced with the last letter, the second with the
# second-last, and so on.

# An Atbash cipher for the Latin alphabet would be as follows:

# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: zyxwvutsrqponmlkjihgfedcba
# It is a very weak cipher because it only has one possible key, and it is a
# simple mono-alphabetic substitution cipher. However, this may not have been an
# issue in the cipher's time.

# Ciphertext is written out in groups of fixed length, the traditional group
# size being 5 letters, leaving numbers unchanged, and punctuation is excluded.
# This is to make it harder to guess things based on word boundaries. All text
# will be encoded as lowercase letters.

# Examples
# - Encoding test gives gvhg
# - Encoding x123 yes gives c123b vh
# - Decoding gvhg gives test
# - Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives
# thequickbrownfoxjumpsoverthelazydog


################################################################################

atbashCipher <- function(text, n, Cipher){
    #removing spaces
    text <- gsub(" ", "", text)

    text <- tolower(text)

    #removing accent
    text <- iconv(text, to = "ASCII//TRANSLIT")

    # removing punctuation
    punctuation <- "[[:punct:]]"
    text <- gsub(punctuation, "", text)

    substitutionCipher <- ""
    for(i in 1:nchar(text)){
        aux <- match(substr(text, i, i), letters) #letters is alphabet in vector
        substitutionCipher <- paste0(substitutionCipher, Cipher[aux])
        # substitutionCipher <- paste(substitutionCipher, Cipher[aux], sep="")
    }

    # group size being n letters
    sequential <- seq(1, nchar(substitutionCipher), n)
    result <- ""
    for(i in 1:length(sequential)){
        result <- paste(
            result,
            substring(substitutionCipher, sequential[i], sequential[i] + n - 1)
        )
    }

    return(result)
}

Cipher <- c("z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j",
            "i","h","g","f","e","d","c","b","a")

print(atbashCipher("Amanda, Thiago e Luísa.", 5, Cipher))

print(atbashCipher("thequickbrownfoxjumpsoverthelazydog.", 5, Cipher))
