from src.agents.graph import app as lg_app

def main():
    allegation = input("Enter allegation: ").strip()
    if not allegation:
        print("No allegation provided. Exiting.")
        return

    result = lg_app.invoke({"allegation": allegation})
    print("\n====== FINAL REBUTTAL ======\n")
    print(result.get("final", result.get("draft", "No output")))

if __name__ == "__main__":
    main()
