--
-- Solution file for the Lua "Hello World" problem
-- Written by Sofia Nieves
-- Thu 26 May 16:52:55 UTC 2016
--

local hello_world = {}

function hello_world.hello(name)
  if name ~= nil then
    return ('Hello, ' .. name .. '!')
  end
  return 'Hello, world!'
end

return hello_world
