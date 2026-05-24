# Smart Affirmation and Goal Suggestion Chatbot

class SmartMotivationBot:

    def __init__(self):

        # Questions to understand user
        self.questions = [
            "What are you interested in?",
            "What is your biggest goal right now?",
            "What do you struggle with the most?",
            "What skill do you want to improve?"
        ]

        self.answers = []

    # Ask user questions
    def ask_questions(self):

        print("====== SMART MOTIVATION BOT ======\n")

        for question in self.questions:

            answer = input(question + " ")
            self.answers.append(answer.lower())

    # Suggest affirmations based on answers
    def suggest_affirmations(self):

        affirmations = []

        combined_answers = " ".join(self.answers)

        if "coding" in combined_answers or "programming" in combined_answers:
            affirmations.append(
                "I am becoming a better programmer every day."
            )

        if "confidence" in combined_answers:
            affirmations.append(
                "I believe in myself and my abilities."
            )

        if "communication" in combined_answers:
            affirmations.append(
                "I express my thoughts clearly and confidently."
            )

        if "study" in combined_answers or "marks" in combined_answers:
            affirmations.append(
                "My hard work will bring success."
            )

        if "stress" in combined_answers or "overthinking" in combined_answers:
            affirmations.append(
                "I am calm, strong, and in control of my thoughts."
            )

        # Default affirmation
        if len(affirmations) == 0:
            affirmations.append(
                "I am growing and improving every day."
            )

        return affirmations

    # Suggest goals based on answers
    def suggest_goals(self):

        goals = []

        combined_answers = " ".join(self.answers)

        if "coding" in combined_answers:
            goals.append("Practice coding for 1 hour")

        if "communication" in combined_answers:
            goals.append("Talk confidently with at least one new person")

        if "study" in combined_answers:
            goals.append("Complete today's study targets")

        if "fitness" in combined_answers:
            goals.append("Exercise for 30 minutes")

        if "stress" in combined_answers:
            goals.append("Take 10 minutes to relax or meditate")

        # Default goal
        if len(goals) == 0:
            goals.append("Do one productive thing today")

        return goals

    # Display suggestions
    def display_results(self):

        affirmations = self.suggest_affirmations()
        goals = self.suggest_goals()

        print("\n====== YOUR PERSONALIZED AFFIRMATIONS ======")

        for affirmation in affirmations:
            print("🌟", affirmation)

        print("\n====== YOUR GOALS FOR TODAY ======")

        for goal in goals:
            print("🎯", goal)

        print("\nKeep going! Small progress is still progress 😄")


# Object Creation
bot = SmartMotivationBot()

# Run chatbot
bot.ask_questions()
bot.display_results()
