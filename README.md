```md
# ⚡ chat-over-sockets

A real-time multi-client chat system built in Python using TCP sockets and select-based I/O. This project demonstrates how real-world messaging systems work at a low level, including client-server architecture, message framing, and handling multiple connections simultaneously.

---

## 🧠 Overview

This project simulates a basic network chat system where multiple clients can connect to a central server and exchange messages in real time. It is designed for learning how backend communication systems and network protocols work internally.

---

## 🚀 Features

- Multi-client support
- Real-time messaging
- TCP socket-based communication
- Custom message framing (header + body)
- Efficient socket handling using `select()`
- Lightweight (no external libraries)

---

## ⚙️ How It Works

- Server listens for incoming client connections
- Each client sends messages with a fixed-size header
- Server reads byte streams from TCP connections
- Messages are broadcast to all connected clients
- `select()` is used to handle multiple sockets efficiently

---

## 📁 Project Structure

```

server.py   → Handles clients and message broadcasting
client.py   → Connects users and sends/receives messages

````

---

## 💻 How to Run

### 1. Start the server
```bash
python server.py
````

### 2. Start client(s)

Open multiple terminals and run:

```bash
python client.py
```

Then enter a username and start chatting.

---

## 💬 Example

```
Alice > Hello everyone
Bob > Hey Alice!
```

---

## 🎯 Purpose

This project is built for learning:

* Socket programming in Python
* TCP/IP communication basics
* Client-server architecture
* Real-time data transfer concepts

---

## 🚀 Future Improvements

* Chat rooms (/join feature)
* Private messaging (/msg)
* Message timestamps
* User authentication
* GUI version (Tkinter or Web UI)
* End-to-end encryption

---

## ⚠️ Notes

* Run server first, then clients
* Works on localhost by default (127.0.0.1)
* Educational project — not production secure

---

## 👨‍💻 Author

Built as a learning project to understand networking and real-time systems in Python.

```
```
