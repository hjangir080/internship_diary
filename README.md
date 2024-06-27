# Internship Diary

This repository contains my Internship Diary project, created using [Mesop](https://google.github.io/mesop/). The diary includes daily reports, weekly reports, a projects section, and a chatbot that can access these reports and provide responses using OpenAI's chat completion. The website is deployed and accessible at [my-internship-diary.onrender.com](https://my-internship-diary.onrender.com).

## Features

- **Daily Reports**: Documents my daily activities and tasks.
- **Weekly Reports**: Summaries of my weekly progress and accomplishments.
- **Projects**: Lists all the projects done during the internship.
- **Chatbot Integration**: An AI-powered chatbot that can respond to queries by accessing my reports.
- **Streaming Responses**: The chatbot now streams its responses for a more interactive experience.

## Technologies Used

- **Mesop**: A framework for creating interactive website with easy to use UI.
- **OpenAI API**: For chat completion and AI responses.
- **Python**
- **Flask**: For connecting the chatbot and handling API requests.
- **Gevent**: For making the application asynchronous.
- **Render**: For deploying the application.

## File Structure

```
├── Daily
│   ├── Daily_1.py
│   ├── Daily_2.py
│   └── ...
├── Weekly
│   ├── Weekly_1.py
│   ├── Weekly_2.py
│   └── ...
├── Projects
│   ├── Projects.py
├── Chatbot
│   └── chatbot.py
├── main.py
├── requirements.txt
├── Procfile
└── README.md
```

## Live Demo

Check out the live version of the project at [my-internship-diary.onrender.com](https://my-internship-diary.onrender.com).


## Acknowledgments

- [Mesop](https://google.github.io/mesop/) for providing the framework.
- [OpenAI](https://openai.com/) for the AI chat completion service.
- [Mesop Demo](https://github.com/google/mesop) for code examples and guidance.
- [Flask](https://flask.palletsprojects.com/) for making web development simpler and more efficient.
- [Gevent](http://www.gevent.org/) for enabling asynchronous functionality.
- [Render](https://render.com/) for deployment services.
