-- A Haskell program that does standard input and output.

{- The "++" operator does string concatenation in Haskell,
NOT integer incrementation. -}
concatToStr x = "It's very nice to meet you, " ++ x ++ "."

main = do
    putStrLn "Hello, what's your name?"
    name <- getLine
    putStrLn (concatToStr name)
    putStrLn "This program written by FUNCTIONAL GANG"
