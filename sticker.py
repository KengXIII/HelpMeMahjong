'''
emptyDeck = []

faTiles = {
  'fa_1' : {
    'file_id' : 'CAACAgIAAxkBAAOFYdae-UKSvhrtzZUrPWCaLo232k8AAjUBAAKMqjQDiRjU3JLdUogjBA'
  },
  'fa_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn4Rh1vPUit-3lJb9__NfFWYKYHjIwAACNQEAAoyqNAOJGNTckt1SiCME'
  },
  'fa_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn4dh1vPvw0FfEo809Zil1fTMchN_FAACNQEAAoyqNAOJGNTckt1SiCME'
  },
  'fa_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn4lh1vQOnX25iJCMr8WonXmniuXhwwACNQEAAoyqNAOJGNTckt1SiCME'
  },
}

zhongTiles = {
  'zhong_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn4th1vlIRtRONjvgcJ4Uc6E_HEHHuAACNwEAAoyqNAPvZw7uvDuMJSME'
  },
  'zhong_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn41h1vlySuxcAAGiJRr7uK0G9LH-6UIAAjcBAAKMqjQD72cO7rw7jCUjBA'
  },
  'zhong_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn49h1vl9XIcXc-jI6YMGTnj4E8BAIQACNwEAAoyqNAPvZw7uvDuMJSME'
  },
  'zhong_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn5Fh1vmI3q_LMHUk33tpfTlouUIxQgACNwEAAoyqNAPvZw7uvDuMJSME'
  },
}

banTiles = {
  'ban_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn5Nh1vpDNb2CLh55SEGFliI6lAeMwgACOQEAAoyqNAMaMvq0_WHDgSME'
  },
  'ban_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn5Vh1vqIZxvv2lXK1AW63LS1Vfm3KgACOQEAAoyqNAMaMvq0_WHDgSME'
  },
  'ban_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn5dh1vqTCo8RUP80tMroMZ4SbfHl6AACOQEAAoyqNAMaMvq0_WHDgSME'
  },
  'ban_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn5lh1vqnAkGA1KRYGXWODtthdRfoowACOQEAAoyqNAMaMvq0_WHDgSME'
  },
}

dongTiles = {
  'dong_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn5th1vq62LEL2jHuk6LKqZ5A19UfQAACeAEAAoyqNAN5PdrZ9-iQYSME'
  },
  'dong_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn51h1vrWXm19bHMyBJ3vk4_o6TAKaQACeAEAAoyqNAN5PdrZ9-iQYSME'
  },
  'dong_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn59h1vrfq7uoVX69hIgk2B0c7o8DtAACeAEAAoyqNAN5PdrZ9-iQYSME'
  },
  'dong_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn6Fh1vroA0SOnnEsyhcDeZLiNoLtUAACeAEAAoyqNAN5PdrZ9-iQYSME'
  },
}

nanTiles = {
  'nan_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn6Nh1vsKU3QkJCh0Kg-tlp_M4p1p8AACegEAAoyqNAOTFyZNNrJglyME'
  },
  'nan_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn6Vh1vs2m9Z2RHLxqB9plJm9LvOoJwACegEAAoyqNAOTFyZNNrJglyME'
  },
  'nan_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn6dh1vtAj1b34sOdBKXBfU7Z2wQWSAACegEAAoyqNAOTFyZNNrJglyME'
  },
  'nan_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn6lh1vtNdl1J3BrJp4MfdwV-YrGBvgACegEAAoyqNAOTFyZNNrJglyME'
  },
}

xiTiles = {
  'xi_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn69h1v3Pr4tzJXhQuZSAz44xGYicxwACfAEAAoyqNAONkZcSq1_PTSME'
  },
  'xi_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn7Fh1v3zck2ZBB12d822dZnZ2RFhSQACfAEAAoyqNAONkZcSq1_PTSME'
  },
  'xi_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn7Nh1v3-j7FL-PLGM326pK2_denKwwACfAEAAoyqNAONkZcSq1_PTSME'
  },
  'xi_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn7Vh1v4KkV6TGLw0PHqEynPgwFctdQACfAEAAoyqNAONkZcSq1_PTSME'
  },
}

beiTiles = {
  'bei_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn7dh1v4va9GfQS9QW_kAAfDPvFJu1tMAAn4BAAKMqjQDf8oBplAvg_sjBA'
  },
  'bei_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn7lh1v47BkEeh-8npCzZWB28sjYKIgACfgEAAoyqNAN_ygGmUC-D-yME'
  },
  'bei_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn7th1v5EkZBg6lrquT-HttILOTVoWgACfgEAAoyqNAN_ygGmUC-D-yME'
  },
  'bei_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn71h1v5NlVCnPVQFR1AMe2066RVz_AACfgEAAoyqNAN_ygGmUC-D-yME'
  },
}

wan1Tiles = {
  'wan-1_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn8Zh1v8X9mFMKuw9ea-Sy-SvJB3bQgACPAEAAoyqNAMBe2QpNfoBlSME'
  },
  'wan-1_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn8hh1v_52E3_1lagF75PCsHaVRevqwACPAEAAoyqNAMBe2QpNfoBlSME'
  },
  'wan-1_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn8ph1wABA3NLfalAXE6uCWYCQMRqwQ0AAjwBAAKMqjQDAXtkKTX6AZUjBA'
  },
  'wan-1_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn85h1wABGVMT7ksX9T6yiYGqAxFqE5YAAjwBAAKMqjQDAXtkKTX6AZUjBA'
  },
}

wan2Tiles = {
  'wan-2_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn9Bh1wABPWIqxrdR4w1nnBtFta09hxAAAj4BAAKMqjQDYLwBtTmot08jBA'
  },
  'wan-2_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn9Jh1wABTn8cug-I8YFDPJ1TvbzuRukAAj4BAAKMqjQDYLwBtTmot08jBA'
  },
  'wan-2_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn9Rh1wABWCfPNnkCox2n-KUAASZSiqfyAAI-AQACjKo0A2C8AbU5qLdPIwQ'
  },
  'wan-2_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn9Zh1wABYXgiK7oI6p-noREglvxNu9oAAj4BAAKMqjQDYLwBtTmot08jBA'
  },
}

wan3Tiles = {
  'wan-3_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn9ph1wABjscrQrVaaNiR9nh3hz4397EAAkABAAKMqjQDiuRMjVIggWEjBA'
  },
  'wan-3_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn9xh1wABl-EQjspvL9zpWHpEuOwYmpAAAkABAAKMqjQDiuRMjVIggWEjBA'
  },
  'wan-3_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn95h1wABoSQAAXE_xBlLZIJW2-_KOtlyAAJAAQACjKo0A4rkTI1SIIFhIwQ'
  },
  'wan-3_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn-Bh1wABqj3il2s0TXKK1Dy0aV9xvEoAAkABAAKMqjQDiuRMjVIggWEjBA'
  },
}

wan4Tiles = {
  'wan-4_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn-xh1wFVheXEozqD0Cvg6rgEuULbHQACQgEAAoyqNAPnBxFkQdGhEiME'
  },
  'wan-4_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn-ph1wFMZe46lnFNUbzfsLYdwapF3AACQgEAAoyqNAPnBxFkQdGhEiME'
  },
  'wan-4_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn-Zh1wFDNLv2jb40atuQLI6ulDknQQACQgEAAoyqNAPnBxFkQdGhEiME'
  },
  'wan-4_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDn-Rh1wE5SYymOGQfJxteUvWq_X5uHgACQgEAAoyqNAPnBxFkQdGhEiME'
  },
}

wan5Tiles = {
  'wan-5_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDn_Jh1wF0s8F7wptZ0RzQrooFXanNLAACRAEAAoyqNANjpKvW6gd-OSME'
  },
  'wan-5_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDn_xh1wGPPpWmHZK-Byn4mj8XlFBSUQACRAEAAoyqNANjpKvW6gd-OSME'
  },
  'wan-5_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDn_5h1wGXoNhLQN0Vfvl1Us1Ysq9MIwACRAEAAoyqNANjpKvW6gd-OSME'
  },
  'wan-5_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoAABYdcBoMGNbK1nhTANb8a-971iZasAAkQBAAKMqjQDY6Sr1uoHfjkjBA'
  },
}

wan6Tiles = {
  'wan-6_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoAJh1wG_friJIlGd4CJkG1zcjG5_-AACSAEAAoyqNAMCynukvmv8eCME'
  },
  'wan-6_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoARh1wHIfXhvm4qX-wABu9PGQDjy9UgAAkgBAAKMqjQDAsp7pL5r_HgjBA'
  },
  'wan-6_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoAZh1wHQv6grJxSXuDWuzSDB6qH4ogACSAEAAoyqNAMCynukvmv8eCME'
  },
  'wan-6_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoAhh1wHoBNWfoX875ZiJZyWHbD3qIgACSAEAAoyqNAMCynukvmv8eCME'
  },
}

wan7Tiles = {
  'wan-7_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoAph1wH-o1Sd3Nyq22j_e3CDsFcl6wACSgEAAoyqNAPlX8OGpITVJCME'
  },
  'wan-7_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoAxh1wIHCI9QmwzvIElVKu_3TKLEQwACSgEAAoyqNAPlX8OGpITVJCME'
  },
  'wan-7_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoA5h1wIQwa1o1ESAQ2grDgxjHmRHRgACSgEAAoyqNAPlX8OGpITVJCME'
  },
  'wan-7_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoBBh1wIYsbZcFOVvIye26zD8f7j8egACSgEAAoyqNAPlX8OGpITVJCME'
  },
}

wan8Tiles = {
  'wan-8_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoBJh1wIjwj45N5vx2H-BGkg_sJle5QACTAEAAoyqNAMfdFGqLJAPkyME'
  },
  'wan-8_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoBhh1wI6egzTEgiMAAE1nJ7awOYdJBwAAkwBAAKMqjQDH3RRqiyQD5MjBA'
  },
  'wan-8_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoBph1wJDNJe8sMeXqAzwnocqm_WqZgACTAEAAoyqNAMfdFGqLJAPkyME'
  },
  'wan-8_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoBxh1wJNGeSZRWBnUzW13poerErXQAACTAEAAoyqNAMfdFGqLJAPkyME'
  },
}

wan9Tiles = {
  'wan-9_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoB5h1wJmgbARFMFQXRxWy1tGNRjqRwACTgEAAoyqNAP41PHRx21lAiME'
  },
  'wan-9_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoCBh1wJwmTqvR1CNxCix7QcRZJKHhAACTgEAAoyqNAP41PHRx21lAiME'
  },
  'wan-9_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoCJh1wJ6qlh92FRui2_3BKBKNziSCQACTgEAAoyqNAP41PHRx21lAiME'
  },
  'wan-9_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoCRh1wKDkpsKLxjKZh5FPjF-B1XBjAACTgEAAoyqNAP41PHRx21lAiME'
  },
}

tong1Tiles = {
  'tong-1_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoCZh1wMQ_o7ED35PjKzDxaXHyoAKwwACUAEAAoyqNAPGaNr9twRSRCME'
  },
  'tong-1_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoChh1wMU5RS7njc1lPnf2pcGXEpaGQACUAEAAoyqNAPGaNr9twRSRCME'
  },
  'tong-1_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoCph1wMXtnQYS-s8UagzBRqexiwbYwACUAEAAoyqNAPGaNr9twRSRCME'
  },
  'tong-1_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoCxh1wMa19u6QMCOBFfz4NkKKQXXaQACUAEAAoyqNAPGaNr9twRSRCME'
  },
}

tong2Tiles = {
  'tong-2_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoC5h1wNqqHZBBTjwZYT2rYQ6UpN8GQACUgEAAoyqNAOmZHjKkqr_bSME'
  },
  'tong-2_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoDBh1wNu1_PKM3uELtg7khuC4TG-nwACUgEAAoyqNAOmZHjKkqr_bSME'
  },
  'tong-2_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoDJh1wNyUaLHln3XzF32DDW7TTtQXAACUgEAAoyqNAOmZHjKkqr_bSME'
  },
  'tong-2_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoDRh1wN1eynSbO9L6RcRX7hTk3fMuwACUgEAAoyqNAOmZHjKkqr_bSME'
  },
}

tong3Tiles = {
  'tong-3_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoDZh1wOymo3UjbBIdCVFg3lB8GMzYAACVAEAAoyqNAPYp0dRianB6CME'
  },
  'tong-3_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoDhh1wO2vCc6SAY4zQNqmRYoql7rfQACVAEAAoyqNAPYp0dRianB6CME'
  },
  'tong-3_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoDph1wO5Jq1jwUAVmqKFBpB_sn7C2gACVAEAAoyqNAPYp0dRianB6CME'
  },
  'tong-3_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoDxh1wO8leYsHk7YIOIC1MHCcFF4dQACVAEAAoyqNAPYp0dRianB6CME'
  },
}

tong4Tiles = {
  'tong-4_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoD5h1wPbq8F9-S30bKP0VPaX7BS6QAACVgEAAoyqNAMcMs7PiB83syME'
  },
  'tong-4_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoEBh1wPehaiQQeTlbNP50c5tGE1klgACVgEAAoyqNAMcMs7PiB83syME'
  },
  'tong-4_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoEJh1wPhoJuC1Uh7HadV9mNZU7OmjgACVgEAAoyqNAMcMs7PiB83syME'
  },
  'tong-4_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoERh1wPkdvi7Og07OqKQ52dEWoRWtQACVgEAAoyqNAMcMs7PiB83syME'
  },
}

tong5Tiles = {
  'tong-5_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoEhh1wQp7Ow8l2LgG0ZpBPnkXmB24AACWAEAAoyqNAMBPD1QqGxWwCME'
  },
  'tong-5_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoEph1wQsNld5I8waHobmC_Bi8tsmfAACWAEAAoyqNAMBPD1QqGxWwCME'
  },
  'tong-5_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoExh1wQuwmxONoFGS9IQYwE_are4cAACWAEAAoyqNAMBPD1QqGxWwCME'
  },
  'tong-5_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoE5h1wQxgXbAblCHRpTtD74a9bpDEQACWAEAAoyqNAMBPD1QqGxWwCME'
  },
}

tong6Tiles = {
  'tong-6_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoFRh1wTQ-7Z0k2w4Cca06EiJaMPTmAACXAEAAoyqNAPUXnZT1YZIsiME'
  },
  'tong-6_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoFZh1wTTq_wut-9ZJ1rZY9lSWB41rwACXAEAAoyqNAPUXnZT1YZIsiME'
  },
  'tong-6_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoFhh1wTWtiiDjZUWXVVB6e28asz_rwACXAEAAoyqNAPUXnZT1YZIsiME'
  },
  'tong-6_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoFph1wTZj3S4ycHnFVyySSnNmDeZgwACXAEAAoyqNAPUXnZT1YZIsiME'
  },
}

tong7Tiles = {
  'tong-7_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoFxh1wUKOZbc9vwAAe3bwtlv7512jM4AAl4BAAKMqjQDXq8JHu-9ZJgjBA'
  },
  'tong-7_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoF5h1wUNLst9zw2HijzTaRQl24_kWQACXgEAAoyqNANerwke771kmCME'
  },
  'tong-7_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoGBh1wUPCw52qgHdeVNvy2447QABf3EAAl4BAAKMqjQDXq8JHu-9ZJgjBA'
  },
  'tong-7_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoGJh1wUSSsO4xD8e4CddcK3WyVU_mgACXgEAAoyqNANerwke771kmCME'
  },
}

tong8Tiles = {
  'tong-8_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoGRh1wVBBfa4cGpX_LSlPLqwGz47BQACYAEAAoyqNANqELSsNSrzeSME'
  },
  'tong-8_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoGZh1wVDDdFN5-c7gGPJCV8Q3kFbVQACYAEAAoyqNANqELSsNSrzeSME'
  },
  'tong-8_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoGhh1wVGX1M123mXQoEvYigHgymohwACYAEAAoyqNANqELSsNSrzeSME'
  },
  'tong-8_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoGph1wVJgpu5OtBNd0I5E-HXbsS46wACYAEAAoyqNANqELSsNSrzeSME'
  },
}

tong9Tiles = {
  'tong-9_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoGxh1wV2j16jp5Pwc1CxL6BDAQu43AACYgEAAoyqNAOjTUjkfo7mRiME'
  },
  'tong-9_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoG5h1wV5mDOkWqcSWFcqW5hocaIUvgACYgEAAoyqNAOjTUjkfo7mRiME'
  },
  'tong-9_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoHBh1wV8goJUEPfnAYaFaEjBShisgAACYgEAAoyqNAOjTUjkfo7mRiME'
  },
  'tong-9_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoHJh1wV_nFXMFa2wA0xafdCw2gKi3gACYgEAAoyqNAOjTUjkfo7mRiME'
  },
}

tiao1Tiles = {
  'tiao-1_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoHRh1wZkFqJ8yrBKgu6Lw766odU_NwACZAEAAoyqNAOzAAFJ5lIx6uUjBA'
  },
  'tiao-1_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoHZh1wZnKmEFwByB2C4TjlZZP-JUBQACZAEAAoyqNAOzAAFJ5lIx6uUjBA'
  },
  'tiao-1_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoHhh1wZpWny5vNZWMxawHuuuBK5HwAACZAEAAoyqNAOzAAFJ5lIx6uUjBA'
  },
  'tiao-1_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoHph1wZrbxINCk19ev2WFqo1LLACPAACZAEAAoyqNAOzAAFJ5lIx6uUjBA'
  },
}

tiao2Tiles = {
  'tiao-1_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoHxh1wbOAaLgRwABA5BVdl_J-XUkrU0AAmYBAAKMqjQDN0BCAAHVa9xeIwQ'
  },
  'tiao-2_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoH5h1wbSSRlPKT5-bW4Eqejg_8jY-gACZgEAAoyqNAM3QEIAAdVr3F4jBA'
  },
  'tiao-2_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoIBh1wbUT0ssSGt7P5i1OxqU1y2-EgACZgEAAoyqNAM3QEIAAdVr3F4jBA'
  },
  'tiao-2_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoIJh1wbWgH8cq7PBWp3q3mAa5WvYtQACZgEAAoyqNAM3QEIAAdVr3F4jBA'
  },
}

tiao3Tiles = {
  'tiao-3_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoIRh1wcTmq-CygbYyAvAuoJehlHlXgACaAEAAoyqNAPKm9syoI2BYSME'
  },
  'tiao-3_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoIZh1wcV9cJ_byRf2Sgq09pMEe1EgwACaAEAAoyqNAPKm9syoI2BYSME'
  },
  'tiao-3_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoIhh1wcXX4h7ljTB62aBr72kQS_2FwACaAEAAoyqNAPKm9syoI2BYSME'
  },
  'tiao-3_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoIph1wcaTqTOOvA7LoStm9Nx39x2EgACaAEAAoyqNAPKm9syoI2BYSME'
  },
}

tiao4Tiles = {
  'tiao-4_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoIxh1wdfQ3WnKK4i5GI0mz_Ppq0waAACagEAAoyqNAP_eI20zhX8OSME'
  },
  'tiao-4_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoI5h1wdiN-Sw6pEnNumzIt86DblXKgACagEAAoyqNAP_eI20zhX8OSME'
  },
  'tiao-4_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJBh1wdjrowp8_dD78v_CwNu72GVdQACagEAAoyqNAP_eI20zhX8OSME'
  },
  'tiao-4_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJJh1wdlFxX79DuiboN7D1QQLQABvhcAAmoBAAKMqjQD_3iNtM4V_DkjBA'
  },
}

tiao5Tiles = {
  'tiao-5_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJRh1wevmotzC-JU08fQdAb0XxbEcAACbAEAAoyqNAP0Y9JDQggeWCME'
  },
  'tiao-5_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJZh1weydi8YCPWHa-uh5A79Clj9UgACbAEAAoyqNAP0Y9JDQggeWCME'
  },
  'tiao-5_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJhh1we0maq-iKr7dldf2FTFLlRHXAACbAEAAoyqNAP0Y9JDQggeWCME'
  },
  'tiao-5_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJph1we2KaCiCJ0aoA4xEdkxs__y8wACbAEAAoyqNAP0Y9JDQggeWCME'
  },
}

tiao6Tiles = {
  'tiao-6_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJxh1whLi7DKsY-MlhNKazyytkwVmAACcAEAAoyqNAMhs8QWxR3AmSME'
  },
  'tiao-6_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoJ5h1whOsZfC69MdNWFLpgtlqQxpAQACcAEAAoyqNAMhs8QWxR3AmSME'
  },
  'tiao-6_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoKBh1whPrLBr7bRu4CISJS7WHnPJOwACcAEAAoyqNAMhs8QWxR3AmSME'
  },
  'tiao-6_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoKJh1whTjUKjVyoOeVtXI9NYZgNE-AACcAEAAoyqNAMhs8QWxR3AmSME'
  },
}

tiao7Tiles = {
  'tiao-7_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoKZh1wh6ZxCGrfmcHNem9W6bhSesNgACcgEAAoyqNAPgvsjEO36SzCME'
  },
  'tiao-7_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoKhh1wh9PvgFPusydcwDaGW-fYHxrwACcgEAAoyqNAPgvsjEO36SzCME'
  },
  'tiao-7_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoKph1wh_UjjtATQlIcwifYphLTkF6wACcgEAAoyqNAPgvsjEO36SzCME'
  },
  'tiao-7_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoKxh1wiBUhElgcwpMQuuBcMpxEfikAACcgEAAoyqNAPgvsjEO36SzCME'
  },
}

tiao8Tiles = {
  'tiao-8_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoLBh1wiuEYdo_GlB3xNFk4ux-C9a7wACdAEAAoyqNAPixMvJ7Qz-ZSME'
  },
  'tiao-8_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoLJh1wiwhnkn1n2C5U4XihObPDhpVQACdAEAAoyqNAPixMvJ7Qz-ZSME'
  },
  'tiao-8_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoLRh1wiyspL761wlxFR_Wek_tdB-wgACdAEAAoyqNAPixMvJ7Qz-ZSME'
  },
  'tiao-8_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoLZh1wi1TAlqxJI7wckTcvWkTTUMeQACdAEAAoyqNAPixMvJ7Qz-ZSME'
  },
}

tiao9Tiles = {
  'tiao-9_1' : {
    'file_id' : 'CAACAgIAAxkBAAEDoLph1wjlqDzJmW9J8cxp9kwkqTjmtQACdgEAAoyqNAOJE3Du0zKtSyME'
  },
  'tiao-9_2' : {
    'file_id' : 'CAACAgIAAxkBAAEDoLxh1wjniW_H5FOVj7j709QHOH-l1wACdgEAAoyqNAOJE3Du0zKtSyME'
  },
  'tiao-9_3' : {
    'file_id' : 'CAACAgIAAxkBAAEDoL5h1wjpHukKsQwsVkC-VOtORuEoxQACdgEAAoyqNAOJE3Du0zKtSyME'
  },
  'tiao-9_4' : {
    'file_id' : 'CAACAgIAAxkBAAEDoMBh1wjrOAABglzqTEv6wmC6yeFU9vcAAnYBAAKMqjQDiRNw7tMyrUsjBA'
  },
}

uniqueTileSet = [faTiles, zhongTiles, banTiles, wan1Tiles, wan2Tiles, wan3Tiles, wan4Tiles, wan5Tiles, wan6Tiles, wan7Tiles, wan8Tiles, wan9Tiles, tong1Tiles, tong2Tiles, tong3Tiles, tong4Tiles, tong5Tiles, tong6Tiles, tong7Tiles, tong8Tiles, tong9Tiles, tiao1Tiles,tiao2Tiles, tiao3Tiles, tiao4Tiles, tiao5Tiles, tiao6Tiles, tiao7Tiles, tiao8Tiles,tiao9Tiles, dongTiles, nanTiles, xiTiles, beiTiles]

# Initial Deck
fullDeck = {**faTiles, **zhongTiles, **banTiles, **wan1Tiles, **wan2Tiles, **wan3Tiles, **wan4Tiles, **wan5Tiles, **wan6Tiles, **wan7Tiles, **wan8Tiles, **wan9Tiles, **tong1Tiles, **tong2Tiles, **tong3Tiles, **tong4Tiles, **tong5Tiles, **tong6Tiles, **tong7Tiles, **tong8Tiles, **tong9Tiles, **tiao1Tiles, **tiao2Tiles, **tiao3Tiles, **tiao4Tiles, **tiao5Tiles, **tiao6Tiles, **tiao7Tiles, **tiao8Tiles, **tiao9Tiles, **dongTiles, **nanTiles, **xiTiles, **beiTiles}
'''

dictOld = {
  "dong" : "CAACAgIAAxkBAAPYYdakM2SPPRPZrPZNowqw_GqiTRUAAngBAAKMqjQDeT3a2ffokGEjBA",
  "nan" : "CAACAgIAAxkBAAPaYdakPCpZ3Ed0JjHHoONakGsIsokAAnoBAAKMqjQDkxcmTTayYJcjBA",
  "xi" : "CAACAgIAAxkBAAPcYdakSVhze0JwdSusB7ROIf3lkgMAAnwBAAKMqjQDjZGXEqtfz00jBA",
  "bei" : "CAACAgIAAxkBAAPeYdakU9IO3PASF-ZiIZDXfZDvH8IAAn4BAAKMqjQDf8oBplAvg_sjBA",
  "fa" : "CAACAgIAAxkBAAOFYdae-UKSvhrtzZUrPWCaLo232k8AAjUBAAKMqjQDiRjU3JLdUogjBA",
  "zhong" : "CAACAgIAAxkBAAOlYdahpmrArE9efVNrmWpLeBhO1CsAAjcBAAKMqjQD72cO7rw7jCUjBA",
  "bai" : "CAACAgIAAxkBAAOnYdah3uEAAenGKgEvujBZhE70QwHjAAI5AQACjKo0Axoy-rT9YcOBIwQ",
  "1wan" : "CAACAgIAAxkBAAOpYdah8Jzz6tuMustgGg_YaLRXktMAAjwBAAKMqjQDAXtkKTX6AZUjBA",
  "2wan" : "CAACAgIAAxkBAAOrYdaiB7pQsXdSz7FKYS8Dm9C76WgAAj4BAAKMqjQDYLwBtTmot08jBA",
  "3wan" : "CAACAgIAAxkBAAOtYdaiJ5GBado5t5VNn0d9p0AXOvoAAkABAAKMqjQDiuRMjVIggWEjBA",
  "4wan" : "CAACAgIAAxkBAAOvYdaiy7ikaiZ-K2Shr1eVFUM3n9wAAkIBAAKMqjQD5wcRZEHRoRIjBA",
  "5wan" : "CAACAgIAAxkBAAOxYdai1mjh8MKRdgbhqRu-Wq95SQ4AAkQBAAKMqjQDY6Sr1uoHfjkjBA",
  "6wan" : "CAACAgIAAxkBAAOzYdai4j_ucJ7HZdYgHufMKuA5h7kAAkgBAAKMqjQDAsp7pL5r_HgjBA",
  "7wan" : "CAACAgIAAxkBAAO1Ydai7UejGMAcqp_3iZkuOrECLeQAAkoBAAKMqjQD5V_DhqSE1SQjBA",
  "8wan" : "CAACAgIAAxkBAAO3Ydai_-XN1_f0AAFEuPqfuapHldD8AAJMAQACjKo0Ax90UaoskA-TIwQ",
  "9wan" : "CAACAgIAAxkBAAO5YdajC9IhdnJAzNY9kc_OhmgvYl0AAk4BAAKMqjQD-NTx0cdtZQIjBA",
  "1tiao" : "CAACAgIAAxkBAAEDoZ1h1-qI1-ASHFudM2kl0D9nD9ArpAACZAEAAoyqNAOzAAFJ5lIx6uUjBA",
  "2tiao" : "CAACAgIAAxkBAAEDoZ9h1-qfBGltyAGp9L7zpi3GPo71lwACZgEAAoyqNAM3QEIAAdVr3F4jBA",
  "3tiao" : "CAACAgIAAxkBAAEDoaFh1-qsSZBVxjUE3cui8bswDXHnGQACaAEAAoyqNAPKm9syoI2BYSME",
  "4tiao" : "CAACAgIAAxkBAAEDoaNh1-q5kz5XnHnxE2VKHiKU8nU55QACagEAAoyqNAP_eI20zhX8OSME",
  "5tiao" : "CAACAgIAAxkBAAEDoaVh1-rHaVOXwEwFNEG2PmKyXT7YCgACbAEAAoyqNAP0Y9JDQggeWCME",
  "6tiao" : "CAACAgIAAxkBAAEDoadh1-rU4kbb7Y2-eJpsxWvTXkSfswACcAEAAoyqNAMhs8QWxR3AmSME",
  "7tiao" : "CAACAgIAAxkBAAEDoalh1-reOupgXQa1rholo3v1AhpGIgACcgEAAoyqNAPgvsjEO36SzCME",
  "8tiao" : "CAACAgIAAxkBAAEDoath1-royknWF_aS_-JaKVR2hnX_AAN0AQACjKo0A-LEy8ntDP5lIwQ",
  "9tiao" : "CAACAgIAAxkBAAEDoa1h1-rxGqQEMnJlaiW__sZvMBuj-gACdgEAAoyqNAOJE3Du0zKtSyME",
  "1tong" : "CAACAgIAAxkBAAEDoa9h1-r94ve4iNyxymuBXvjTpeTSKgACUAEAAoyqNAPGaNr9twRSRCME",
  "2tong" : "CAACAgIAAxkBAAEDobFh1-sHKmQ0rgmuI6HY0FNwN-ckNAACUgEAAoyqNAOmZHjKkqr_bSME",
  "3tong" : "CAACAgIAAxkBAAEDobNh1-sQRqnvvKMmMKlzsXhtBJyFhAACVAEAAoyqNAPYp0dRianB6CME",
  "4tong" : "CAACAgIAAxkBAAEDobVh1-sZE7-hB5wG1kBSkMsNxUae3AACVgEAAoyqNAMcMs7PiB83syME",
  "5tong" : "CAACAgIAAxkBAAEDobdh1-slQ75Rg7Sr-rm9hFJEvS_g4wACWAEAAoyqNAMBPD1QqGxWwCME",
  "6tong" : "CAACAgIAAxkBAAEDoblh1-syT9j_oeGyflwQQOqm9e1_2AACXAEAAoyqNAPUXnZT1YZIsiME",
  "7tong" : "CAACAgIAAxkBAAEDobth1-s7h6sRsqeiajkZlOEAASWjZIoAAl4BAAKMqjQDXq8JHu-9ZJgjBA",
  "8tong" : "CAACAgIAAxkBAAEDob1h1-tHqVGmrWNjtMou9fxyTj_Y1QACYAEAAoyqNANqELSsNSrzeSME",
  "9tong" : "CAACAgIAAxkBAAEDob9h1-tRrA9WooljHy0ojosUq8594gACYgEAAoyqNAOjTUjkfo7mRiME",
}

dict = {
  "dong" : "AgADeAEAAoyqNAM",
  "nan" : "AgADegEAAoyqNAM",
  "xi" : "AgADfAEAAoyqNAM",
  "bei" : "AgADfgEAAoyqNAM",
  "fa" : "AgADNQEAAoyqNAM",
  "zhong" : "AgADNwEAAoyqNAM",
  "bai" : "AgADOQEAAoyqNAM",
  "1wan" : "AgADPAEAAoyqNAM",
  "2wan" : "AgADPgEAAoyqNAM",
  "3wan" : "AgADQAEAAoyqNAM",
  "4wan" : "AgADQgEAAoyqNAM",
  "5wan" : "AgADRAEAAoyqNAM",
  "6wan" : "AgADSAEAAoyqNAM",
  "7wan" : "AgADSgEAAoyqNAM",
  "8wan" : "AgADTAEAAoyqNAM",
  "9wan" : "AgADTgEAAoyqNAM",
  "1tiao" : "AgADZAEAAoyqNAM",
  "2tiao" : "AgADZgEAAoyqNAM",
  "3tiao" : "AgADaAEAAoyqNAM",
  "4tiao" : "AgADagEAAoyqNAM",
  "5tiao" : "AgADbAEAAoyqNAM",
  "6tiao" : "AgADcAEAAoyqNAM",
  "7tiao" : "AgADcgEAAoyqNAM",
  "8tiao" : "AgADdAEAAoyqNAM",
  "9tiao" : "AgADdgEAAoyqNAM",
  "1tong" : "AgADUAEAAoyqNAM",
  "2tong" : "AgADUgEAAoyqNAM",
  "3tong" : "AgADVAEAAoyqNAM",
  "4tong" : "AgADVgEAAoyqNAM",
  "5tong" : "AgADWAEAAoyqNAM",
  "6tong" : "AgADXAEAAoyqNAM",
  "7tong" : "AgADXgEAAoyqNAM",
  "8tong" : "AgADYAEAAoyqNAM",
  "9tong" : "AgADYgEAAoyqNAM",
}

tupleOfTiles = dict.items()

