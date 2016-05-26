--
-- Solution for "accumulate" Lua problem
-- Written by Sofia Nieves
-- Thu 26 May 18:03:24 UTC 2016
--

return function(collection, operation)
  local result = {}
  for i, element in ipairs(collection) do
    table.insert(result, operation(collection[i]))
  end
  return result
end

