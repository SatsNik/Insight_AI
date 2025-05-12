/**
 * Form validation script for Insight AI
 */

document.addEventListener('DOMContentLoaded', function() {
    // Fetch all forms that need validation
    const forms = document.querySelectorAll('.needs-validation');
    
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        }, false);
        
        // Add input event listeners for real-time validation feedback
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                if (this.checkValidity()) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                } else {
                    this.classList.remove('is-valid');
                    this.classList.add('is-invalid');
                }
            });
        });
    });
    
    // Numeric input validation for specific inputs
    const numericInputs = document.querySelectorAll('input[type="number"]');
    numericInputs.forEach(input => {
        // Set min/max constraints from HTML attributes
        const min = parseInt(input.getAttribute('min'));
        const max = parseInt(input.getAttribute('max'));
        
        input.addEventListener('input', function() {
            let value = parseInt(this.value);
            
            // Validate min/max if they exist
            if (!isNaN(min) && value < min) {
                this.setCustomValidity(`Value should be at least ${min}`);
            } else if (!isNaN(max) && value > max) {
                this.setCustomValidity(`Value should be at most ${max}`);
            } else {
                this.setCustomValidity('');
            }
        });
    });
    
    // Student Performance form specific validation
    const studentForm = document.getElementById('studentForm');
    if (studentForm) {
        const readingScore = document.getElementById('reading_score');
        const writingScore = document.getElementById('writing_score');
        
        // Validate scores are between 0-100
        [readingScore, writingScore].forEach(input => {
            input.addEventListener('input', function() {
                const value = parseInt(this.value);
                if (isNaN(value)) {
                    this.setCustomValidity('Please enter a valid number');
                } else if (value < 0) {
                    this.setCustomValidity('Score cannot be negative');
                } else if (value > 100) {
                    this.setCustomValidity('Score cannot exceed 100');
                } else {
                    this.setCustomValidity('');
                }
            });
        });
    }
    
    // Ad View form specific validation
    const adviewForm = document.getElementById('adviewForm');
    if (adviewForm) {
        const views = document.getElementById('views');
        const likes = document.getElementById('likes');
        const dislikes = document.getElementById('dislikes');
        const comments = document.getElementById('comment_count');
        
        // Ensure all numeric values are non-negative
        [views, likes, dislikes, comments].forEach(input => {
            input.addEventListener('input', function() {
                const value = parseInt(this.value);
                if (isNaN(value)) {
                    this.setCustomValidity('Please enter a valid number');
                } else if (value < 0) {
                    this.setCustomValidity('Value cannot be negative');
                } else {
                    this.setCustomValidity('');
                }
            });
        });
        
        // Additional validation for logical constraints
        views.addEventListener('input', function() {
            const viewsValue = parseInt(this.value);
            const likesValue = parseInt(likes.value);
            const dislikesValue = parseInt(dislikes.value);
            
            if (!isNaN(viewsValue) && !isNaN(likesValue) && !isNaN(dislikesValue)) {
                if (likesValue + dislikesValue > viewsValue) {
                    this.setCustomValidity('Total likes and dislikes cannot exceed total views');
                } else {
                    this.setCustomValidity('');
                }
            }
        });
    }
});
