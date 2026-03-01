{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e2981cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Unit Converter ---\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    print(\"\\n--- Unit Converter ---\")\n",
    "    convert_from = input(\"Enter starting unit (inches, feet, yards) or 'q' to quit: \").lower()\n",
    "    \n",
    "    # Check if the user wants to exit\n",
    "    if convert_from == 'q':\n",
    "        print(\"Goodbye!\")\n",
    "        break\n",
    "\n",
    "    convert_to = input(\"Enter unit to convert to (inches, feet, yards): \").lower()\n",
    "\n",
    "    if convert_from in ['inches', 'in', 'inch']:\n",
    "        number_of_inches = float(input(\"Enter number of inches to convert: \"))\n",
    "        if convert_to in ['feet', 'ft', 'foot']:\n",
    "            print(number_of_inches, 'in', '=', number_of_inches * 0.0833333, 'ft')\n",
    "        elif convert_to in ['yards', 'yd', 'yards']:\n",
    "            print(number_of_inches, 'in', '=', number_of_inches * 0.0277778, 'yd')\n",
    "        else:\n",
    "            print('Wrong input for target unit')\n",
    "\n",
    "    elif convert_from in ['feet', 'ft', 'foot']:\n",
    "        number_of_feet = float(input(\"Enter number of feet to convert: \"))\n",
    "        if convert_to in ['inches', 'in', 'inch']:\n",
    "            print(number_of_feet, 'ft', '=', number_of_feet * 12, 'in')\n",
    "        elif convert_to in ['yards', 'yd', 'yards']:\n",
    "            print(number_of_feet, 'ft', '=', number_of_feet * 0.333333, 'yd')\n",
    "        else:\n",
    "            print('Wrong input for target unit')\n",
    "\n",
    "    elif convert_from in ['yards', 'yd', 'yards']:\n",
    "        number_of_yards = float(input(\"Enter number of yards to convert: \"))\n",
    "        if convert_to in ['inches', 'in', 'inch']:\n",
    "            print(number_of_yards, 'yd', '=', number_of_yards * 36, 'in')\n",
    "        elif convert_to in ['feet', 'ft', 'foot']:\n",
    "            print(number_of_yards, 'yd', '=', number_of_yards * 3, 'ft')\n",
    "        else:\n",
    "            print('Wrong input for target unit')\n",
    "            \n",
    "    else:\n",
    "        print('Please enter Inches, Feet or Yards')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
