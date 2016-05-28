--
-- Solution for "hamming" in Lua
-- Written by Sofia Nieves
-- Sat 28 May 06:38:26 UTC 2016
--

local hamming = {}

function hamming.compute(strand1, strand2)
  local distance = 0

  for i = 1, string.len(strand1) do
    if string.sub(strand1, i, i) ~= string.sub(strand2, i, i) then
      distance = distance + 1
    end
  end

  return distance 
end

return hamming

