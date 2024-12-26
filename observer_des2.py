# The Subject (Publisher)
class Subject:
    def __init__(self):
        self.observers = []  # List to keep track of observers (subscribers)

    def subscribe(self, observer):
        self.observers.append(observer)  # Add an observer
        print(f"{observer.name} has subscribed.")

    def unsubscribe(self, observer):
        self.observers.remove(observer)  # Remove an observer
        print(f"{observer.name} has unsubscribed.")

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)  # Notify all observers with a message


# The Observer (Subscriber)
class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received update: {message}")


# Example usage
if __name__ == "__main__":
    # Create a Subject
    news_publisher = Subject()

    # Create Observers
    subscriber1 = Observer("Alice")
    subscriber2 = Observer("Bob")
    subscriber3 = Observer("Charlie")

    # Subscribe Observers to the Subject
    news_publisher.subscribe(subscriber1)
    news_publisher.subscribe(subscriber2)

    # Publish a notification
    news_publisher.notify("Breaking News: Observer Pattern Explained!")

    # Unsubscribe one Observer
    news_publisher.unsubscribe(subscriber2)

    # Publish another notification
    news_publisher.notify("Update: More on Design Patterns!")
