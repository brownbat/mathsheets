# MathSheets

A web-based elementary math worksheet generator that creates customized practice problems for addition, subtraction, multiplication, and division, optimized for classroom use.

**Live Demo**: [https://mathsheets.onrender.com](https://mathsheets.onrender.com)

## Features

- **Specialized Problem Types**: Choose from 19 different operation subtypes grouped by educational concepts
- **Educational Categories**: Problems grouped by key concepts (carrying, regrouping, etc.)
- **Vertical Problem Layout**: Properly formatted vertical problems for all operations
- **Multiple Pages**: Clean pagination with proper headers on each page
- **Print-Optimized**: Designed specifically for printing classroom worksheets
- **Student Information**: Fields for student name and date 
- **Flexible Problem Count**: Choose from 10, 20, 30, 40, or 50 problems

## Operation Categories
- **Addition**: 1-digit, 2-digit + 1-digit, without carrying, with carrying, mixed
- **Subtraction**: numbers 1-20, from multiples of 10, without regrouping, with regrouping, mixed
- **Multiplication**: by 2/5/10, by 3/4/6, by 7/8/9, mixed facts, 2-digit × 1-digit
- **Division**: facts to 10, facts to 20, larger ÷ 1-digit (with/without remainder), larger ÷ 2-digit

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to http://127.0.0.1:5000/

## Deployment

This application is currently deployed on Render. For your own deployment:

1. Fork or clone this repository
2. Connect your GitHub repository to Render
3. Create a new Web Service with these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variable**: Set `PORT` to match your service provider's requirements

Note: On free tier Render services, the application may take 30-60 seconds to "wake up" after periods of inactivity.

## Future Enhancements

- Answer key generation
- PDF download option
- Mixed operation worksheets
- Word problem generation
- Worksheet themes for different grade levels