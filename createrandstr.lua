function CreateRandStr(length)
  local length = length or 0
  if length <= 0 then
    return nil
  end


  local random_strs = {}
  if length > 0 then
    math.randomseed(os.time())
    for i=1, length do
      local a = math.random(97,122)
      local c = math.random(65,90)
      local i = math.random(48,57)
      local w = math.random(1,3)
      if w == 1 then table.insert(random_strs, string.char(a)) end
      if w == 2 then table.insert(random_strs, string.char(c)) end
      if w == 3 then table.insert(random_strs, string.char(i)) end
    end
  end

  return table.concat(random_strs, "")


end

CreateRandStr(10)
