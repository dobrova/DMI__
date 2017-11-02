#!/bin/bash

function calc_bin ()
{
sk=$input

	while [ $sk -ne 0 ]
	do
		sk_bin+=`expr $sk % 2`
		sk=`expr $sk / 2`
	done

	printf " Dec_sk = $input\n"
	printf " Bin_sk = "
	printf "$sk_bin" | rev

	calc_Hex $input
	calc_Oct $input
}

function calc_Hex ()
{
sk=$input

	while [ $sk -ne 0 ]
	do
		sk_Hex_mod=`expr $sk % 16`
		case $sk_Hex_mod in
			10)
			sk_Hex+=A
			;;

			11)
			sk_Hex+=B
			;;

                        12)
                        sk_Hex+=C
                        ;;

                        13)
                        sk_Hex+=D
                        ;;

                        14)
                        sk_Hex+=E
                        ;;

                        15)
                        sk_Hex+=F
                        ;;

			*)
			sk_Hex+=`expr $sk % 16`
			;;
		esac

		sk=`expr $sk / 16`

	done
	printf " Hex_sk = "
	printf "$sk_Hex" | rev
}

function calc_Oct ()
{
sk=$input

	while [ $sk -ne 0 ]
	do
		oct_Mod=`expr $sk % 8`
		sk=`expr $sk / 8`
		sk_Oct+=$oct_Mod
	done

printf " Oct_sk = "
printf "$sk_Oct" | rev
}

function input ()
{
	clear;
	printf "Skaitlis decimala forma: "
	read input
	calc_bin $input
}

input
