# We meed this so we can skip ugly casting down below
from __future__ import division # Python3 thingy

global foods
foods = {}
foods[2328] = (84, "Gulp.")
foods[2362] = (48, "Yum.")
foods[2666] = (180, "Munch.")
foods[2667] = (144, "Munch.")
foods[2668] = (120, "Mmmm.")
foods[2669] = (204, "Munch.")
foods[2670] = (48, "Gulp.")
foods[2671] = (360, "Chomp.")
foods[2672] = (720, "Chomp.")
foods[2673] = (60, "Yum.")
foods[2674] = (72, "Yum.")
foods[2675] = (156, "Yum.")
foods[2676] = (96, "Yum.")
foods[2677] = (12, "Yum.")
foods[2678] = (216, "Slurp.")
foods[2679] = (12, "Yum.")
foods[2680] = (24, "Yum.")
foods[2681] = (108, "Yum.")
foods[2682] = (240, "Yum.")
foods[2683] = (204, "Munch.")
foods[2684] = (60, "Crunch.")
foods[2685] = (72, "Munch.")
foods[2686] = (108, "Crunch.")
foods[2687] = (24, "Crunch.")
foods[2688] = (24, "Mmmm.")
foods[2689] = (120, "Crunch.")
foods[2690] = (72, "Crunch.")
foods[2691] = (96, "Crunch.")
foods[2695] = (72, "Gulp.")
foods[2696] = (108, "Smack.")
foods[2769] = (60, "Crunch.")
foods[2787] = (108, "Crunch.")
foods[2788] = (48, "Crunch.")
foods[2789] = (264, "Munch.")
foods[2790] = (360, "Crunch.")
foods[2791] = (108, "Crunch.")
foods[2792] = (72, "Crunch.")
foods[2793] = (144, "Crunch.")
foods[2794] = (36, "Crunch.")
foods[2795] = (432, "Crunch.")
foods[2796] = (300, "Crunch.")
foods[5097] = (48, "Yum.")
foods[5678] = (96, "Gulp.")
foods[6125] = (96, "Mmmm.")
foods[6278] = (120, "Mmmm.")
foods[6279] = (180, "Mmmm.")
foods[6393] = (144, "Mmmm.")
foods[6394] = (180, "Mmmm.")
foods[6501] = (240, "Mmmm.")
foods[6541] = (72, "Gulp.")
foods[6542] = (72, "Gulp.")
foods[6543] = (72, "Gulp.")
foods[6544] = (72, "Gulp.")
foods[6545] = (72, "Gulp.")
foods[6569] = (12, "Mmmm.")
foods[6574] = (60, "Mmmm.")
foods[7158] = (300, "Munch.")
foods[7159] = (180, "Munch.")
foods[7372] = (0, "Yummy.")
foods[7373] = (0, "Yummy.")
foods[7374] = (0, "Yummy.")
foods[7375] = (0, "Yummy.")
foods[7376] = (0, "Yummy.")
foods[7377] = (0, "Yummy.")
foods[7963] = (720, "Munch.")
foods[8838] = (120, "Gulp.")
foods[8839] = (60, "Yum.")
foods[8840] = (12, "Yum.")
foods[8841] = (12, "Urgh.")
foods[8842] = (84, "Munch.")
foods[8843] = (60, "Crunch.")
foods[8844] = (12, "Gulp.")
foods[8845] = (60, "Munch.")
foods[8847] = (132, "Yum.")
foods[9005] = (88, "Slurp.")
foods[9996] = (0, "Slurp.")
foods[10454] = (0, "Your head begins to feel better.")
foods[11136] = (120, "Mmmm.")
foods[11246] = (180, "Yum.")
foods[11370] = (36, "Urgh.")

def onUse(creature, thing, position, **a):
    global foods
    gainhp = creature.getVocation().health
    gainmana = creature.getVocation().mana
    duration = foods[thing.itemId][0]
    sound = foods[thing.itemId][1]
    someCondition = creature.getCondition(CONDITION_REGENERATEHEALTH)    

    if thing.count > 0 and (not someCondition or someCondition.length + gainmana[1] <= 1500):
        thing.count -= 1
        creature.replaceItem(position, thing)
        creature.condition(Condition(CONDITION_REGENERATEHEALTH, 0, duration, gainhp[1], gainhp=gainhp[0] * creature.getRegainRate()), CONDITION_ADD, 1500)
        creature.condition(Condition(CONDITION_REGENERATEMANA, 0, duration, gainmana[1], gainmana=gainhp[0] * creature.getRegainRate()), CONDITION_ADD, 1500)
        creature.say(sound, 'MSG_SPEAK_MONSTER_SAY')
    elif someCondition and (someCondition.length >= 1500 or someCondition.length + gainmana[1] > 1500):
        creature.cancelMessage("You are full.")
    if thing.count == 0:
        creature.removeItem(position)        

reg('use', foods.keys(), onUse)