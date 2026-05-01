"""
Climate Finance Content Automation - Main Application
Flask-based API server for content generation, scheduling, and analytics
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.content.generator import ContentGenerator
from src.scheduler.scheduler import PostScheduler
from src.analytics.tracker import AnalyticsTracker
from src.utils.logger import get_logger

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up logging
logger = get_logger(__name__)

# Initialize components
content_gen = ContentGenerator()
scheduler = PostScheduler()
analytics = AnalyticsTracker()


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'climate-content-automation'
    }), 200


@app.route('/api/content/generate', methods=['POST'])
def generate_content():
    """Generate climate finance content."""
    try:
        data = request.json
        topic = data.get('topic', 'carbon_markets')
        content_format = data.get('format', 'linkedin_post')
        tone = data.get('tone', 'professional')
        length = data.get('length', 'medium')

        result = content_gen.generate(
            topic=topic,
            format=content_format,
            tone=tone,
            length=length
        )

        return jsonify({
            'status': 'success',
            'data': result
        }), 200

    except Exception as e:
        logger.error(f"Content generation error: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500


@app.route('/api/content/topics', methods=['GET'])
def get_topics():
    """Get available climate finance topics."""
    try:
        topics = content_gen.get_available_topics()
        return jsonify({
            'status': 'success',
            'topics': topics
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500


@app.route('/api/schedule/post', methods=['POST'])
def schedule_post():
    """Schedule a post for publishing."""
    try:
        data = request.json

        result = scheduler.schedule_post(
            content=data.get('content'),
            platforms=data.get('platforms', ['linkedin']),
            scheduled_time=data.get('scheduled_time'),
            title=data.get('title'),
            image_url=data.get('image_url'),
            metadata=data.get('metadata')
        )

        return jsonify(result), 201

    except Exception as e:
        logger.error(f"Scheduling error: {str(e)}")
        return jsonify({'status': 'error', 'error': str(e)}), 500


@app.route('/api/schedule/posts', methods=['GET'])
def get_scheduled_posts():
    """Get all scheduled posts."""
    try:
        status = request.args.get('status')
        posts = scheduler.get_scheduled_posts(status=status)
        return jsonify({
            'status': 'success',
            'posts': posts
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500


@app.route('/api/schedule/post/<post_id>', methods=['DELETE'])
def cancel_post(post_id):
    """Cancel a scheduled post."""
    try:
        result = scheduler.cancel_post(post_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 400


@app.route('/api/analytics/dashboard', methods=['GET'])
def analytics_dashboard():
    """Get analytics dashboard."""
    try:
        metrics = analytics.get_performance_metrics()
        return jsonify({
            'status': 'success',
            'metrics': metrics
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500


@app.route('/api/analytics/trending', methods=['GET'])
def get_trending_topics():
    """Get trending climate finance topics."""
    try:
        trending = analytics.get_trending_topics()
        return jsonify({
            'status': 'success',
            'trending': trending
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'status': 'error',
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'status': 'error',
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)
