if "":
    # So sánh với traditional method
    import matplotlib.pyplot as plt

    # Data for comparison
    methods = ["Rule-Based", "BERT", "LLaMA-2-7b", "LLaMA-3-8b", "LLaMA-3.1-8b"]
    accuracy = [50, 70, 85, 89, 92]
    manual_effort = [9, 7, 4, 3, 2]  # Scale of manual effort (lower is better)
    complex_json = [3, 6, 8, 9, 10]  # Ability to handle complex JSON (higher is better)

    # Plotting accuracy comparison
    plt.figure(figsize=(10, 6))
    plt.bar(methods, accuracy, color=["red", "orange", "yellow", "lightgreen", "green"])
    plt.title("Accuracy Comparison Between Traditional and Modern Methods")
    plt.ylabel("Accuracy (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

    # Plot manual effort and JSON complexity handling
    plt.figure(figsize=(10, 6))
    plt.plot(methods, manual_effort, marker='o', linestyle='--', label="Manual Effort (Lower Better)", color="red")
    plt.plot(methods, complex_json, marker='s', linestyle='-', label="Complex JSON Handling", color="blue")
    plt.title("Manual Effort vs. Complex JSON Handling")
    plt.ylabel("Scale (1-10)")
    plt.legend()
    plt.tight_layout()
    plt.show()

if "":
    # So sánh BERT methods
    import matplotlib.pyplot as plt

    # Data for comparison
    methods = ["BERT", "LLaMA-2-7b", "LLaMA-3-8b", "LLaMA-3.1-8b"]
    accuracy = [88, 85, 89, 92]  # Example accuracy values
    computational_cost = [9, 4, 5, 6]  # Scale from 1 (low) to 10 (high), representing computational cost
    domain_adaptation = [6, 8, 9, 9]  # Scale for domain adaptation (1 = poor, 10 = excellent)
    training_time = [100, 72, 65, 60]  # Training time in hours

    # Create subplots for comparison
    fig, ax = plt.subplots(2, 2, figsize=(12, 10))

    # Accuracy comparison
    ax[0, 0].bar(methods, accuracy, color=['red', 'yellow', 'lightgreen', 'green'])
    ax[0, 0].set_title('Accuracy Comparison')
    ax[0, 0].set_ylabel('Accuracy (%)')
    ax[0, 0].set_ylim(0, 100)

    # Computational cost comparison (lower is better)
    ax[0, 1].bar(methods, computational_cost, color=['red', 'yellow', 'lightgreen', 'green'])
    ax[0, 1].set_title('Computational Cost (Lower is Better)')
    ax[0, 1].set_ylabel('Cost (Scale 1-10)')
    ax[0, 1].set_ylim(0, 10)

    # Domain adaptation comparison
    ax[1, 0].bar(methods, domain_adaptation, color=['red', 'yellow', 'lightgreen', 'green'])
    ax[1, 0].set_title('Domain Adaptation (Higher is Better)')
    ax[1, 0].set_ylabel('Adaptation (Scale 1-10)')
    ax[1, 0].set_ylim(0, 10)

    # Training time comparison
    ax[1, 1].bar(methods, training_time, color=['red', 'yellow', 'lightgreen', 'green'])
    ax[1, 1].set_title('Training Time Comparison (Lower is Better)')
    ax[1, 1].set_ylabel('Training Time (Hours)')
    ax[1, 1].set_ylim(0, 120)
    plt.legend()
    # Adjust layout and save
    plt.tight_layout()
    # plt.savefig('/mnt/data/comparison_chart.png')
    plt.show()

if "So sánh với Recent LLMs techniques":
    # So sánh với Recent LLMs techniques
    import matplotlib.pyplot as plt

    # # Data for comparison
    # methods = ["BERT", "LLaMA-2-7b", "LLaMA-3-8b", "LLaMA-3.1-8b"]
    # accuracy = [88, 85, 89, 92]  # Example accuracy values
    # computational_cost = [9, 4, 5, 6]  # Scale from 1 (low) to 10 (high), representing computational cost
    # domain_adaptation = [6, 8, 9, 9]  # Scale for domain adaptation (1 = poor, 10 = excellent)
    # training_time = [100, 72, 65, 60]  # Training time in hours

    # # Create subplots for comparison
    # fig, ax = plt.subplots(2, 2, figsize=(12, 10))

    # # Accuracy comparison
    # ax[0, 0].bar(methods, accuracy, color=['red', 'yellow', 'lightgreen', 'green'])
    # ax[0, 0].set_title('Accuracy Comparison')
    # ax[0, 0].set_ylabel('Accuracy (%)')
    # ax[0, 0].set_ylim(0, 100)

    # # Computational cost comparison (lower is better)
    # ax[0, 1].bar(methods, computational_cost, color=['red', 'yellow', 'lightgreen', 'green'])
    # ax[0, 1].set_title('Computational Cost (Lower is Better)')
    # ax[0, 1].set_ylabel('Cost (Scale 1-10)')
    # ax[0, 1].set_ylim(0, 10)

    # # Domain adaptation comparison
    # ax[1, 0].bar(methods, domain_adaptation, color=['red', 'yellow', 'lightgreen', 'green'])
    # ax[1, 0].set_title('Domain Adaptation (Higher is Better)')
    # ax[1, 0].set_ylabel('Adaptation (Scale 1-10)')
    # ax[1, 0].set_ylim(0, 10)

    # # Training time comparison
    # ax[1, 1].bar(methods, training_time, color=['red', 'yellow', 'lightgreen', 'green'])
    # ax[1, 1].set_title('Training Time Comparison (Lower is Better)')
    # ax[1, 1].set_ylabel('Training Time (Hours)')
    # ax[1, 1].set_ylim(0, 120)

    # # Adjust layout and save
    # plt.tight_layout()
    # # plt.savefig('/mnt/data/comparison_chart_v2.png')
    # plt.show()

    # Data for comparison of LLMs in JSON extraction tasks
    models = ["GPT-3", "GPT-4", "LLaMA-2-7b", "LLaMA-3-8b", "LLaMA-3.1-8b"]
    accuracy = [85, 88, 85, 89, 92]  # Accuracy percentages
    computational_cost = [9, 8, 6, 5, 4]  # Computational cost scale (higher is worse)
    structured_output = [6, 7, 8, 9, 9.5]  # Ability to handle JSON structured output (scale 1-10)

    # Create a figure with subplots
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    # Plot 1: Accuracy Comparison
    ax[0].bar(models, accuracy, color=["red", "orange", "yellow", "lightgreen", "green"])
    ax[0].set_title("Accuracy Comparison")
    ax[0].set_ylabel("Accuracy (%)")
    ax[0].set_ylim(0, 100)

    # Plot 2: Computational Cost (Lower is Better)
    ax[1].bar(models, computational_cost, color=["red", "orange", "yellow", "lightgreen", "green"])
    ax[1].set_title("Computational Cost")
    ax[1].set_ylabel("Cost Scale (1-10)")
    # ax[1].invert_yaxis()  # Invert to show lower values as better

    # Plot 3: Structured Output Capability
    ax[2].bar(models, structured_output, color=["red", "orange", "yellow", "lightgreen", "green"])
    ax[2].set_title("Structured Output Capability")
    ax[2].set_ylabel("JSON Handling (Scale 1-10)")
    ax[2].set_ylim(0, 10)

    # Adjust layout and save the chart
    plt.tight_layout()
    # plt.savefig('/mnt/data/llm_json_comparison.png')
    plt.show()



