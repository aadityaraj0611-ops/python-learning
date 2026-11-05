
import string


def clean_word(word):
    return word.strip(string.punctuation).lower()


def analyze_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        lines = text.splitlines()
        words = text.split()

        word_frequency = {}

        for word in words:
            cleaned = clean_word(word)

            if cleaned != "":
                if cleaned in word_frequency:
                    word_frequency[cleaned] += 1
                else:
                    word_frequency[cleaned] = 1

        unique_words = set(word_frequency.keys())
        valid_words = list(word_frequency.keys())

        total_characters = len(text)
        total_words = len(words)
        total_lines = len(lines)
        total_sentences = 0

        for character in text:
            if character in ".!?":
                total_sentences += 1

        if len(valid_words) > 0:
            longest_word = max(valid_words, key=len)
            shortest_word = min(valid_words, key=len)

            most_common_word = max(
                word_frequency,
                key=word_frequency.get
            )

            highest_frequency = word_frequency[most_common_word]

        else:
            longest_word = "None"
            shortest_word = "None"
            most_common_word = "None"
            highest_frequency = 0

        print("\n========== FILE ANALYSIS ==========")
        print("File name:", filename)
        print("Total characters:", total_characters)
        print("Total words:", total_words)
        print("Total lines:", total_lines)
        print("Total sentences:", total_sentences)
        print("Unique words:", len(unique_words))
        print("Longest word:", longest_word)
        print("Shortest word:", shortest_word)
        print("Most frequent word:", most_common_word)
        print("Frequency:", highest_frequency)

        search_word = input("\nEnter a word to search: ").strip().lower()

        if search_word in word_frequency:
            search_result = (
                "Occurrences: "
                + str(word_frequency[search_word])
            )
            print(
                search_word,
                "appears",
                word_frequency[search_word],
                "time(s)."
            )
        else:
            search_result = "Word not found."
            print("Word not found in the file.")

        report = "========== TEXT FILE ANALYSIS REPORT ==========\n"
        report += "File name: " + filename + "\n"
        report += "Total characters: " + str(total_characters) + "\n"
        report += "Total words: " + str(total_words) + "\n"
        report += "Total lines: " + str(total_lines) + "\n"
        report += "Total sentences: " + str(total_sentences) + "\n"
        report += "Unique words: " + str(len(unique_words)) + "\n"
        report += "Longest word: " + longest_word + "\n"
        report += "Shortest word: " + shortest_word + "\n"
        report += "Most frequent word: " + most_common_word + "\n"
        report += "Frequency: " + str(highest_frequency) + "\n"

        report += "\n========== WORD FREQUENCIES ==========\n"

        for word in word_frequency:
            report += word + ": " + str(word_frequency[word]) + "\n"

        report += "\n========== WORD SEARCH RESULT ==========\n"
        report += "Search word: " + search_word + "\n"
        report += search_result + "\n"

        with open("analysis_report.txt", "w", encoding="utf-8") as file:
            file.write(report)

        print("\nReport generated successfully: analysis_report.txt")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except UnicodeDecodeError:
        print("Error: Unable to read the file encoding.")


print("====== TEXT FILE ANALYZER ======")

filename = input("Enter the text file name: ").strip()

analyze_file(filename)
