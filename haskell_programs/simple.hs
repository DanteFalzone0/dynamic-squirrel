-- some very simple purely functional Haskell functions
twoTimes x = x + x
fourTimes x = twoTimes (twoTimes x)

isEven x = if mod x 2 == 0 then True else False
-- "mod x 2" in Haskell is like "x % 2" in other languages

isOdd x = if not (isEven x) then True else False
