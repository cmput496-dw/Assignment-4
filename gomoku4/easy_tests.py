#################################################
#						#
#	            VERY EASY			#
#						#
#################################################

#Full board, 2 open positions, only one good play
clear_board
play B D4
play W E4
play B F4
play W E3
play B E5
play W C3
play B F5
play W D5
play B F3
play W F2
play B D6
play W C7
play B C6
play W E6
play B C4
play W A1
play B B4
play W F6
play B C2
play W D2
play B B2
play W E2
play B G2
play W D1
play B C1
play W B6
play B G7
play W E7
play B G4
play W G3
play B B3
play W D3
play B E1
play W A6
play B F1
play W G6
play B B1
play W A3
play B A4
play W C5
play B A5
play W F7
play B D7
play W B7
play B A7
play W G1
showboard
10 test
#?[play b B5]


#################################################
#						#
#	              EASY			#
#						#
#################################################

#Easy 5 in-a-row win
boardsize 7
play b A1
play w G1
play b B2
play w G7
play b C3
play w A7
play b D4
play w F6
showboard
20 test
#?[play b E5]

#Easy 5 in-a-row block
clear_board
play b A1
play w D1
play b G1
play w D2
play b G7
play w D3
play b A7
play w D4
showboard
30 test
#?[play b D5]

#Play stone to win vs opponent with 3 in-a-row on board
clear_board
play b B5
play w A1
play b C5
play w A2
play b D5
play w A3
play b E5
play w G1
showboard
40 test
#?[play b A5|F5]

#Block opponents win with 3 in-a-row on board
clear_board
play b A1
play w F4
play b A2
play w F5
play b A3
play w F6
play b A7
play w F7
showboard
50 test
#?[play b F3]

#Play stone to win game vs opponent with 4 in-a-row on board
clear_board
play b b6
play w b7
play b c5
play w c7
play b d4
play w d7
play b e3
play w e7
showboard
60 test
#?[play b A7|F2]



