CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR,
    phone VARCHAR,
    handicapped BOOLEAN NOT NULL DEFAULT FALSE,
    vip BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS parking_spots (
    id SERIAL PRIMARY KEY,
    vip BOOLEAN NOT NULL DEFAULT FALSE,
    handicapped BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS reservations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    spot_id INT NOT NULL,
    start_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    end_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_spot FOREIGN KEY (spot_id) REFERENCES parking_spots(id)
);

INSERT INTO users (id, email, phone, handicapped, vip) VALUES
('11111111-1111-1111-1111-111111111111', 'peter.griffin@spoonerstreet.com', '555-0101', FALSE, FALSE),
('22222222-2222-2222-2222-222222222222', 'joe.swanson@quahogpd.gov',      '555-0102', TRUE,  FALSE),
('33333333-3333-3333-3333-333333333333', 'glenn.quagmire@quahogair.com',  '555-0103', FALSE, TRUE);

INSERT INTO parking_spots (id, vip, handicapped) VALUES
(1, FALSE, FALSE),
(2, FALSE, FALSE),
(3, TRUE,  FALSE),
(4, TRUE,  FALSE),
(5, FALSE, TRUE),
(6, FALSE, TRUE);

INSERT INTO reservations (id, user_id, spot_id, start_time, end_time) VALUES
('a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1', '11111111-1111-1111-1111-111111111111', 1, '2026-08-10 08:00:00', '2026-08-10 12:00:00'),
('b2b2b2b2-b2b2-b2b2-b2b2-b2b2b2b2b2b2', '11111111-1111-1111-1111-111111111111', 1, '2026-08-10 13:00:00', '2026-08-10 17:00:00'),
('c3c3c3c3-c3c3-c3c3-c3c3-c3c3c3c3c3c3', '22222222-2222-2222-2222-222222222222', 5, '2026-08-10 09:00:00', '2026-08-10 11:00:00'),
('d4d4d4d4-d4d4-d4d4-d4d4-d4d4d4d4d4d4', '33333333-3333-3333-3333-333333333333', 3, '2026-08-10 10:00:00', '2026-08-10 14:00:00');