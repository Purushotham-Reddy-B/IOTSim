# AI Chatbot Setup Guide

## 🤖 Overview

The IoT Simulator now features an intelligent AI chatbot that can:
- Generate custom IoT scripts for any scenario
- Answer questions about simulator features
- Provide troubleshooting assistance
- Handle complex queries like ChatGPT/Claude

## 🚀 Two Modes of Operation

### **1. OpenAI-Powered Mode (Full AI Capabilities)**
- Handles any type of script generation request
- Answers complex questions about the simulator
- Provides intelligent, context-aware responses
- Requires OpenAI API key

### **2. Rule-Based Mode (No API Key Required)**
- Pre-built script templates (smart home, industrial, smart city)
- Predefined Q&A for common questions
- Works without any external dependencies
- Automatic fallback if OpenAI is unavailable

---

## 🔑 Setting Up OpenAI Integration

### **Step 1: Get OpenAI API Key**
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in to your OpenAI account
3. Click "Create new secret key"
4. Copy your API key (starts with `sk-...`)

### **Step 2: Install OpenAI Library**
```bash
pip install openai
```

### **Step 3: Set Environment Variable**

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your_api_key_here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Or create a `.env` file:**
```
OPENAI_API_KEY=your_api_key_here
```

### **Step 4: Restart the Application**
```bash
python app.py
```

---

## 🎯 Using the AI Chatbot

### **Access the Chatbot**
1. Open http://127.0.0.1:5000/editor
2. Click "🤖 AI Assistant" button
3. Type your question or request

### **Example Queries for Script Generation**

**OpenAI Mode (Any custom request):**
- "Create a smart home network with 3 temperature sensors and a central hub"
- "Generate an industrial IoT setup with PLC, sensors, and cloud connectivity"
- "Write a script for agricultural monitoring with soil moisture sensors"
- "Create a healthcare IoT system with patient monitoring devices"
- "Build a smart factory network with conveyor belt sensors and actuators"

**Rule-Based Mode (Pre-built templates):**
- "Create smart home network"
- "Generate industrial IoT script"
- "Build smart city network"
- "Make a simple IoT setup"

### **Example Queries for Q&A**

**OpenAI Mode (Any question):**
- "How do I optimize my network for low power consumption?"
- "What's the best protocol for long-range sensor communication?"
- "How can I simulate packet loss in my network?"
- "Explain the difference between I2C and SPI protocols"
- "How do I debug a script that's not connecting devices properly?"

**Rule-Based Mode (Common questions):**
- "How to use multi-layer view?"
- "What devices are available?"
- "How do I export data?"
- "What protocols are supported?"

---

## 💰 Cost Considerations

### **OpenAI API Costs**
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- **Average chatbot query**: ~100-200 tokens
- **Cost per query**: ~$0.0002-$0.0004
- **1000 queries**: ~$0.20-$0.40

### **Rule-Based Mode**
- **Cost**: Free
- **No API calls required**
- **Works offline**

---

## 🔧 Troubleshooting

### **OpenAI Not Working**
**Problem**: Chatbot uses rule-based mode despite API key

**Solutions**:
1. Verify API key is set correctly
2. Check internet connection
3. Ensure `openai` library is installed: `pip install openai`
4. Check API key has credits: https://platform.openai.com/account/usage

### **Import Error**
**Problem**: `ModuleNotFoundError: No module named 'openai'`

**Solution**:
```bash
pip install openai
```

### **API Key Not Recognized**
**Problem**: "OpenAI not available" message

**Solutions**:
1. Restart terminal after setting environment variable
2. Verify API key format (should start with `sk-`)
3. Check for typos in API key

---

## 🎓 Best Practices

### **For Script Generation**
- Be specific about device types and quantities
- Mention specific protocols if needed
- Describe the network topology
- Include any special requirements (low power, long range, etc.)

### **For Technical Questions**
- Be specific about the feature you're asking about
- Include context about what you're trying to achieve
- Mention any errors you're encountering

---

## 🚀 Advanced Features

### **Custom System Prompt**
The chatbot uses a specialized system prompt that includes:
- All available device classes and methods
- Simulator features and protocols
- Script generation guidelines
- Response style instructions

This ensures the AI provides accurate, simulator-specific responses.

### **Automatic Fallback**
If OpenAI API fails or is unavailable, the system automatically falls back to rule-based responses, ensuring the chatbot always works.

### **Script Insertion**
When the chatbot generates a script, you can click "Insert Script" to automatically add it to the editor.

---

## 📊 Comparison

| **Feature** | **OpenAI Mode** | **Rule-Based Mode** |
|-------------|-----------------|---------------------|
| Custom Scripts | ✅ Any scenario | ❌ Pre-built only |
| Complex Q&A | ✅ Any question | ❌ Predefined only |
| Cost | ~$0.0002 per query | Free |
| Internet Required | ✅ Yes | ❌ No |
| API Key Required | ✅ Yes | ❌ No |
| Response Quality | High | Medium |

---

## 🎯 Recommendation

**For Development/Testing**: Use rule-based mode (free, no setup)
**For Production/Demos**: Use OpenAI mode (full capabilities, impressive demos)
**For Patent Presentation**: Use OpenAI mode (shows advanced AI integration)

---

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your OpenAI API key has credits
3. Ensure all dependencies are installed
4. Check the application logs for error messages

**The AI chatbot is now ready to assist with any IoT simulator-related queries!** 🤖🚀
