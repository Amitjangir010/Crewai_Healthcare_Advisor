# Crewai_Healthcare_Advisor
A friendly healthcare chatbot crew for providing safe home health remedies .

```markdown
**Healthcare Chatbot**

**How to Run the Project**

**Clone the Repository:**
```sh
git clone https://github.com/mitjangir010/Crewai_Healthcare_Advisor.git
cd Crewai_Healthcare_Advisor
```

**Install Requirements:**
```sh
pip install -r requirements.txt
```

**Set Up Environment Variables:**
- Create a `.env` file in the root directory.
- Add your API keys:
  ```
  GOOGLE_API_KEY=your_google_api_key
  SERPER_API_KEY=your_serper_api_key
  ```

**Run the Project:**
- Open `crew.py`.
- Modify the input section with your health-related question.
- Run the script:
  ```sh
  python crew.py
  ```

**Example Input:**
```python
result = crew.kickoff(inputs={'topic': 'I am having headache from last 2 days.'})
print(result)
```

After running, you will receive a comprehensive report with the best home remedies for your query.
```
