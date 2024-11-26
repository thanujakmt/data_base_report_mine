
sender_email = "helpdesk@vmokshagroup.com"
sender_password = "Super$p@ce08"
receiver_email = "thanuja.k@vmokshagroup.com"
# cc_emails = ["CibyP@vmokshagroup.com",
#              "srinivasulu.ayila@vmokshagroup.com","apurva.s@vmokshagroup.com","madhusudhan@vmokshagroup.com",
#              "jyotirmaya@vmokshagroup.com"]
cc_emails = ["thanuja.k@vmokshagroup.com"]

population_list = {
    "usa":341412215,
    "uk":67736802,
    "ca":40081291,
    "au":26439111,
    "dk":5882262,
    "se":10549347,
    "uae":9575190,
    "nz":5269939
}

host = "helenzys-mysql-dev.clyhoefsujtn.us-east-1.rds.amazonaws.com"

# niche_list = [
# 'landscaper',
# 'custom_home_builder',
# 'heating_equipment',
# 'garage_door_supplier',
# 'carpet_installer',
# 'pizza',
# 'pawn_shop',
# 'homeopathy',
# 'aromatherapy',
# 'cranial_sacral_therapy',
# 'sound_healing',
# 'reflexology',
# 'Hypnotherapy',
# 'sound_therapy',
# 'reiki_healers',
# 'herbal_medicine',
# 'functional_medicine',
# 'energy_healer',
# 'ayurveda',
# 'acupuncturists',
# 'chiropractor',
# 'dentist',
# 'mental_health_service',
# 'remodeler',
# 'daycare',
# 'physiotherapist',
# 'yoga_studio',
# 'massage_therapist',
# 'naturopathic_practitioner',
# 'nutritionist',
# 'meditation'
# ]

niche_list = [
    'neurofeedback_biofeedback',
    'aesthetician',
    'osteopath',
    'holistic_health',
    'naprapath',
    'herbalist',
    'dietitian',
    'occupational_therapist',
    'holistic_medicine',
    'wellness_clinics',
    'integrative_medicine',
    'homeopathy',
    'aromatherapy',
    'cranial_sacral_therapy',
    'sound_healing',
    'reflexology',
    'Hypnotherapy',
    'sound_therapy',
    'reiki_healers',
    'herbal_medicine',
    'functional_medicine',
    'energy_healer',
    'ayurveda',
    'acupuncturists',
    'chiropractor',
    'physiotherapist',
    'yoga_studio',
    'massage_therapist',
    'naturopathic_practitioner',
    'nutritionist',
    'meditation'
]

country_code_list = ['usa','ca','uk','au','se','dk','nz','uae']

desired_list = ['Items', 'Total Count', 'Percentage', 
                'usa','usa_usp',
                'ca','ca_usp',
                'uk','uk_usp',
                'au','au_usp',
                'se','se_usp',
                'dk','dk_usp',
                'nz','nz_usp',
                'uae','uae_usp']

# desired_list2 = ['Items', 'Total Count', 'Percentage', 
#                 'usa','usa_per_10k',
#                 'ca','ca_per_10k',
#                 'uk','uk_per_10k',
#                 'au','au_per_10k',
#                 'se','se_per_10k',
#                 'dk','dk_per_10k',
#                 'nz','nz_per_10k',
#                 'uae','uae_per_10k']

# country_code_list = ['usa','au']

db_credential = {"dentist":{"user":"dentist","password":"mis+yOtter56","database":"dentist_business_db"},
                "daycare":{"user":"daycare","password":"qui(kPatch32","database":"daycare_business_db"},
                "remodeler":{"user":"remodeler","password":"f!rstMemory75","database":"remodeler_business_db"},
                "physiotherapist":{"user":"physiotherapist","password":"bumpyButt3r45","database":"physiotherapist_business_db"},
                "chiropractor":{"user":"chiropractor","password":"wackyM3tal66","database":"chiropractor_business_db"},
                "mental_health_service":{"user":"mentalhealthservice","password":"$caryRhino10","database":"mental_health_service_business_data"},
                "acupuncturists":{"user":"usa_acupuncturists_db","password":"mushyL@ke90","database":"usa_acupuncturists_db"},
                "yoga_studio":{"user":"usa_yoga_db","password":"3mptyArt53","database":"usa_yoga_db"},
                "massage_therapist" :{"user":"massage_therapist_business_db","password":"wackyJ3wel31","database":"massage_therapist_business_db"},
                "naturopathic_practitioner" :{"user":"naturopathic_practitioner","password":"ultr@Memory31","database":"naturopathic_practitioner_business_db"},
                "nutritionist" : {"user":"nutritionist_business_db","password":"busyMoos361","database":"nutritionist_business_db"},
                "meditation" : {"user":"meditation_business_db","password":"whit3Berry63","database":"meditation_business_db"},
                "ayurveda" : {"user":"ayurveda_business_db","password":"coldS+eam68","database":"ayurveda_business_db"},
                "energy_healer" : {"user":"energy_healer","password":"s!llyFog66","database":"energy_healer_business_db"},
                "functional_medicine" : {"user":"functional_medicine","password":"(oolBoat12","database":"functional_medicine_business_db"},
                "herbal_medicine" : {"user":"herbal_medicine","password":"]ollySoda92","database":"herbal_medicine_business_db"},
                "reiki_healers" : {"user":"reiki_healers","password":"tinyMuskr@t88","database":"reiki_healers_business_db"},
                "sound_therapy" : {"user":"sound_therapy","password":"nic3Hippo18","database":"sound_therapy_business_db"},
                "Hypnotherapy" : {"user":"Hypnotherapy","password":"s@dGoose21","database":"Hypnotherapy_business_db"},
                "reflexology" : {"user":"reflexology","password":"goldJe@ns18","database":"reflexology_business_db"},
                "sound_healing" : {"user":"sound_healing","password":"hugeB!rd94","database":"sound_healing_business_db"},
                "cranial_sacral_therapy" : {"user":"cranial_sacral","password":"mis+yButton11","database":"cranial_sacral_therapy_business_db"},
                "aromatherapy" : {"user":"aromatherapy","password":"j@deCart56","database":"aromatherapy_business_db"},
                "homeopathy" : {"user":"homeopathy_business","password":"noisyCoyot393","database":"homeopathy_business_db"},
                "pawn_shop" : {"user":"pawn_shop","password":"pal3Jewel72","database":"pawn_shop_business_db"},
                "pizza" : {"user":"pizza_business","password":"wa(kyLight30","database":"pizza_business_db"},
                "carpet_installer" : {"user":"carpet_installer","password":"h@ppyHand41","database":"carpet_installer_business_db"},
                "garage_door_supplier" : {"user":"garage_door_supplier","password":"wh!teCopper65","database":"garage_door_supplier_business_db"},
                "heating_equipment" : {"user":"heating_equipment","password":"$hortIce85","database":"heating_equipment_supplier_db"},
                "custom_home_builder" : {"user":"custom_home_builder","password":"gr3enGate24","database":"custom_home_builder_business_db"},
                "landscaper" : {"user":"landscaper_business","password":"fr3eTest95","database":"landscaper_business_db"},
                "plumber" : {"user":"plumber_business","password":"sw!ftGrip71","database":"plumber_business_db"},
                "integrative_medicine" : {"user":"integrative_medicine","password":"brownAc+or77","database":"integrative_medicine_business_db"},
                "wellness_clinics" : {"user":"wellness_clinics","password":"brav3Pony4","database":"wellness_clinics_business_db"},
                "holistic_medicine" : {"user":"holistic_medicine","password":"grayMi$t30","database":"holistic_medicine_business_db"},
                "occupational_therapist" : {"user":"occupational_therapist","password":"lumpyCav318","database":"occupational_therapist_business_db"},
                "dietitian" : {"user":"dietitian","password":"swee+Knot29","database":"dietitian_business_db"},
                "herbalist" : {"user":"herbalist_business_db","password":"b@dCanary15","database":"herbalist_business_db"},
                "naprapath" : {"user":"naprapath_business_db","password":"r!chJump30","database":"naprapath_business_db"},
                "holistic_health" : {"user":"holistic_health_business_db","password":"k3enGame44","database":"holistic_health_business_db"},
                "osteopath" : {"user":"osteopath_business_db","password":"messyWh@le28","database":"osteopath_business_db"},
                "aesthetician" : {"user":"aesthetician_business_db","password":"qu!ckCamel89","database":"aesthetician_business_db"},
                "neurofeedback_biofeedback" : {"user":"neurofeedback","password":"icycopper23","database":"neurofeedback_biofeedback_business_db"}
                }
