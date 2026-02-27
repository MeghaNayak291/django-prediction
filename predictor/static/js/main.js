// Main JavaScript file for Strawberry Disease Detection

document.addEventListener('DOMContentLoaded', function() {
    console.log('Application loaded successfully');
    
    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});

// Disable submit button animation
function handleFormSubmit(event) {
    const submitBtn = event.target.querySelector('button[type="submit"]');
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
    }
}

// Alert message fade out
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'fadeOut 0.5s ease';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});

// Image preview with drag and drop
const setupImageUpload = () => {
    const imageInput = document.getElementById('imageInput');
    const uploadArea = document.getElementById('uploadArea');
    
    if (imageInput && uploadArea) {
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });

        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });

        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            imageInput.files = e.dataTransfer.files;
        });

        uploadArea.addEventListener('click', () => imageInput.click());
    }
};

document.addEventListener('DOMContentLoaded', setupImageUpload);
