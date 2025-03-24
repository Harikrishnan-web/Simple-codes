#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CANDIDATES 100
#define MAX_NAME_LENGTH 50
#define FILENAME "voting_results.txt"

// Structure to store candidate details
typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    int votes;
} Candidate;

// Array to store candidates
Candidate candidates[MAX_CANDIDATES];
int candidate_count = 0;

// Function to load results from file
void loadResults() {
    FILE *file = fopen(FILENAME, "r");
    if (file == NULL) {
        printf("No previous results found. Starting fresh.\n");
        return;
    }

    candidate_count = 0;
    while (fscanf(file, "%d,%49[^,],%d\n", &candidates[candidate_count].id,
                  candidates[candidate_count].name, &candidates[candidate_count].votes) == 3) {
        candidate_count++;
    }

    fclose(file);
    printf("Results loaded successfully!\n");
}

// Function to save results to file
void saveResults() {
    FILE *file = fopen(FILENAME, "w");
    if (file == NULL) {
        printf("Error saving results to file.\n");
        return;
    }

    for (int i = 0; i < candidate_count; i++) {
        fprintf(file, "%d,%s,%d\n", candidates[i].id, candidates[i].name, candidates[i].votes);
    }

    fclose(file);
    printf("Results saved successfully!\n");
}

// Function to add a candidate
void addCandidate() {
    if (candidate_count >= MAX_CANDIDATES) {
        printf("Maximum number of candidates reached.\n");
        return;
    }

    int id;
    char name[MAX_NAME_LENGTH];

    printf("Enter Candidate ID: ");
    scanf("%d", &id);

    // Check if the ID is unique
    for (int i = 0; i < candidate_count; i++) {
        if (candidates[i].id == id) {
            printf("Candidate ID already exists. Try again.\n");
            return;
        }
    }

    printf("Enter Candidate Name: ");
    getchar();  // Clear input buffer
    fgets(name, MAX_NAME_LENGTH, stdin);
    name[strcspn(name, "\n")] = '\0';  // Remove trailing newline

    candidates[candidate_count].id = id;
    strcpy(candidates[candidate_count].name, name);
    candidates[candidate_count].votes = 0;
    candidate_count++;

    printf("Candidate added successfully!\n");
}

// Function to display all candidates
void displayCandidates() {
    printf("\nCandidates List:\n");
    for (int i = 0; i < candidate_count; i++) {
        printf("ID: %d, Name: %s, Votes: %d\n", candidates[i].id, candidates[i].name, candidates[i].votes);
    }
    if (candidate_count == 0) {
        printf("No candidates available.\n");
    }
}

// Function to cast a vote
void castVote() {
    int voter_id, candidate_id;
    printf("Enter your voter ID (for reference only): ");
    scanf("%d", &voter_id);

    printf("Enter Candidate ID to vote for: ");
    scanf("%d", &candidate_id);

    for (int i = 0; i < candidate_count; i++) {
        if (candidates[i].id == candidate_id) {
            candidates[i].votes++;
            printf("Vote cast successfully for %s.\n", candidates[i].name);
            return;
        }
    }

    printf("Invalid Candidate ID. Vote not counted.\n");
}

// Function to display results
void displayResults() {
    printf("\nVoting Results:\n");
    for (int i = 0; i < candidate_count; i++) {
        printf("Candidate: %s, Votes: %d\n", candidates[i].name, candidates[i].votes);
    }
    if (candidate_count == 0) {
        printf("No results to display.\n");
    }
}

// Main Function
int main() {
    int choice;

    loadResults();

    while (1) {
        printf("\nVoting System Menu:\n");
        printf("1. Add Candidate\n");
        printf("2. Display Candidates\n");
        printf("3. Cast Vote\n");
        printf("4. Display Results\n");
        printf("5. Save and Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            addCandidate();
            break;
        case 2:
            displayCandidates();
            break;
        case 3:
            castVote();
            break;
        case 4:
            displayResults();
            break;
        case 5:
            saveResults();
            printf("Exiting the system. Goodbye!\n");
            exit(0);
        default:
            printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}