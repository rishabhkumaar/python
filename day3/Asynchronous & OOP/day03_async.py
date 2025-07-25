# day03_async.py

import asyncio
from datetime import datetime

class StringPractice:
    def __init__(self):
        self.name = ""
        self.date = ""
        self.text = "This is a string  with some  double spaces."

    async def problem_1(self):
        self.name = await self.get_input("Enter your name: ")
        print(f"Good Afternoon, {self.name}")

    async def problem_2(self):
        self.name = await self.get_input("Enter your name: ")
        self.date = await self.get_input("Enter the date (DD/MM/YYYY): ")
        letter_template = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''
        formatted_letter = letter_template.replace("<|NAME|>", self.name).replace("<|DATE|>", self.date)
        print("\nFormatted Letter:\n")
        print(formatted_letter)

    async def problem_3(self):
        index = self.text.find("  ")
        print("\nFirst occurrence of double spaces is at index:", index)

    async def problem_4(self):
        fixed_text = self.text.replace("  ", " ")
        print("\nString after replacing double spaces:\n", fixed_text)

    async def problem_5(self):
        formatted = "Dear Rishabh,\n\tYou are selected!\n\tThanks and regards,\n\tAdmin"
        print("\nFormatted letter with escape sequences:\n")
        print(formatted)

    async def get_input(self, prompt):
        return await asyncio.to_thread(input, prompt)

    async def run_all(self):
        await self.problem_1()
        await self.problem_2()
        await self.problem_3()
        await self.problem_4()
        await self.problem_5()


if __name__ == "__main__":
    sp = StringPractice()
    asyncio.run(sp.run_all())
