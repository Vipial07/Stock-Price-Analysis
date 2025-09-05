# Stock-Price-Analysis
Stock-Price-Analysis

---

# 🚀 Kafka Local Setup (Beginner Project)

## 📌 Overview

This project is for **beginners who are new to Apache Kafka**.
It demonstrates how to set up **Kafka on a local machine** and run a simple **Producer → Topic → Consumer** pipeline.

---

## 🔧 Prerequisites

* Java 8 or higher (Kafka requires Java)
* Apache Kafka (download from [Kafka Downloads](https://kafka.apache.org/downloads))
* Windows/Linux/Mac machine

## ⚡ Setup Steps

### 1️⃣ Start Zookeeper

Kafka requires **Zookeeper** to manage brokers.
Run the following command from the Kafka directory:

```sh
bin/windows/zookeeper-server-start.bat config/zookeeper.properties   # Windows

---

### 2️⃣ Start Kafka Broker

Open another terminal and start Kafka server:

```sh
bin/windows/kafka-server-start.bat config/server.properties   # Windows
---

### 3️⃣ Create a Kafka Topic

```sh
bin/windows/kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1   # Windows

✅ Verify topic created:

```sh
bin/windows/kafka-topics.bat --list --bootstrap-server localhost:9092   # Windows

### 4️⃣ Start Kafka Producer

```sh
bin/windows/kafka-console-producer.bat --broker-list localhost:9092 --topic test-topic   # Windows

👉 Type a few sample messages in the terminal.

### 5️⃣ Start Kafka Consumer

Open another terminal and run:

```sh
bin/windows/kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test-topic --from-beginning   # Windows

✅ You should see the messages sent by the producer.

## 🎯 Project Outcomes

* Installed and configured **Kafka locally**.
* Learned how to **create topics, produce, and consume messages**.
* Understood the **basic Kafka pipeline**: Producer → Topic → Consumer.

