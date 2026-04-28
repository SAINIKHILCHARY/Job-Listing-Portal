const multer = require('multer');
const path = require('path');
const crypto = require('crypto');

const os = require('os');

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    // Use /tmp directory if running on Vercel, otherwise use local uploads folder
    const uploadPath = process.env.VERCEL ? os.tmpdir() : path.join(__dirname, '..', 'uploads');
    cb(null, uploadPath);
  },
  filename: (req, file, cb) => {
    const uniqueSuffix = crypto.randomBytes(16).toString('hex');
    cb(null, `${uniqueSuffix}${path.extname(file.originalname)}`);
  },
});

const fileFilter = (req, file, cb) => {
  if (file.mimetype === 'application/pdf') {
    cb(null, true);
  } else {
    cb(new Error('Only PDF files are allowed'), false);
  }
};

const upload = multer({
  storage,
  fileFilter,
  limits: { fileSize: parseInt(process.env.MAX_FILE_SIZE) || 5242880 },
});

module.exports = upload;
